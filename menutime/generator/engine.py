import random
from menutime import db
from google.cloud.firestore_v1.base_query import FieldFilter
from datetime import datetime

def meal_selector(user_desired_meals, desired_servings, user_id):
    fish_meals_desired = user_desired_meals[0]
    chicken_meals_desired = user_desired_meals[1]
    beef_meals_desired = user_desired_meals[2]
    salad_meals_desired = user_desired_meals[3]
    taco_meals_desired = user_desired_meals[4]
    vegetarian_meals_desired = user_desired_meals[5]
    fish_ids = []
    chicken_ids = []
    beef_ids = []
    salad_ids = []
    taco_ids = []
    # pasta_ids = []
    vegetarian_ids = []
    this_weeks_ids = []


    meal_query = db.collection("meals")
    meals = [doc.to_dict() for doc in meal_query.stream()]
    for temp_meal in meals:
        if temp_meal['category'] == 'fish':
            fish_ids.append(temp_meal['id'])
        elif temp_meal['category'] == 'chicken':
            chicken_ids.append(temp_meal['id'])
        elif temp_meal['category'] == 'beef':
            beef_ids.append(temp_meal['id'])
        elif temp_meal['category'] == 'salad':
            salad_ids.append(temp_meal['id'])
        elif temp_meal['category'] == 'taco':
            taco_ids.append(temp_meal['id'])
        elif temp_meal['category'] == 'vegetarian':
            vegetarian_ids.append(temp_meal['id'])
        else:
            pass
    
    fish_meal_id = random.sample(fish_ids, fish_meals_desired)
    chicken_meal_id = random.sample(chicken_ids, chicken_meals_desired)
    beef_meal_id = random.sample(beef_ids, beef_meals_desired)
    salad_meal_id = random.sample(salad_ids, salad_meals_desired)
    taco_meal_id = random.sample(taco_ids, taco_meals_desired)
    vegetarian_meal_id = random.sample(vegetarian_ids, vegetarian_meals_desired)

    this_weeks_ids = fish_meal_id + chicken_meal_id + beef_meal_id + salad_meal_id + taco_meal_id + vegetarian_meal_id
    db.collection("selections").add({
                    "user_id": user_id,
                    "meal_selections": user_desired_meals,
                    "meal_portions": desired_servings,
                    "meal_ids_returned": this_weeks_ids,
                    "created_date": datetime.utcnow()
                               })

    return this_weeks_ids

def populate_shopping_list(this_weeks_ids, desired_servings):

    menu_meal_names = []
    menu_ingredients = []
    menu_description = []
    menu_link = []
    menu_servings = []
    menu_image_url = []

    for id in this_weeks_ids:
        query = db.collection('meals').where(filter=FieldFilter('id', '==', id))
        menu_obj = [doc.to_dict() for doc in query.stream()]
        menu_meal_names.append(menu_obj[0]['name'])
        menu_ingredients.append(menu_obj[0]['ingredients'])
        menu_description.append(menu_obj[0]['description'])
        menu_link.append(menu_obj[0]['link'])
        menu_servings.append(menu_obj[0]['servings']) 
        menu_image_url.append(menu_obj[0]['image_url'])

    temp_list = {}
    for (meal, serving) in zip(menu_ingredients, menu_servings):
        for ingredient in meal:
            ingredient_name = ingredient.split("-")[0]
            ingredient_amount = (float(ingredient.split("-")[1]) / float(serving)) * float(desired_servings)
            ingredient_type = ingredient.split("-")[2]
            if ingredient_name not in temp_list:
                temp_list[ingredient_name] = (f"{round(ingredient_amount,2)} - {ingredient_type}")
            else:
                temp_amount = float(temp_list[ingredient_name].split("-")[0])
                temp_amount += float(ingredient_amount)
                temp_list[ingredient_name] = (f"{round(temp_amount,2)} - {ingredient_type}")

    shopping_list = ''
    for key in temp_list:
        shopping_list += str(f"{key} - {temp_list[key]}, ")
    shopping_list = shopping_list[:-2]

    temp_list = []
    protein_list = {}
    produce_list = {}
    refrigerator_list = {}
    dry_goods_list = {}
    spices_list = {}
    dressing_list = {}
    frozen_list = {}
    other_list = {}
    proteins = [result.to_dict() for result in db.collection("ingredients").where(filter=FieldFilter('proteins', "!=", "")).stream()][0]['proteins']
    produce = [result.to_dict() for result in db.collection("ingredients").where(filter=FieldFilter('produce', "!=", "")).stream()][0]['produce']
    refrigerator = [result.to_dict() for result in db.collection("ingredients").where(filter=FieldFilter('refrigerator', "!=", "")).stream()][0]['refrigerator']
    dry_goods = [result.to_dict() for result in db.collection("ingredients").where(filter=FieldFilter('dry_goods', "!=", "")).stream()][0]['dry_goods']
    dressing = [result.to_dict() for result in db.collection("ingredients").where(filter=FieldFilter('dressing', "!=", "")).stream()][0]['dressing']
    spices = [result.to_dict() for result in db.collection("ingredients").where(filter=FieldFilter('spices', "!=", "")).stream()][0]['spices']
    other = [result.to_dict() for result in db.collection("ingredients").where(filter=FieldFilter('other', "!=", "")).stream()][0]['other']
    ingredient_list_types = [proteins, produce, refrigerator, dry_goods, dressing, spices, other]
    brokenout_lists = [protein_list, produce_list, refrigerator_list, dry_goods_list, dressing_list, frozen_list, spices_list, other_list]
    brokenout_lists_str = ['protein_list', 'produce_list', 'refrigerator_list', 'dry_goods_list', 'dressing_list', 'frozen_list', 'spices_list', 'other_list']

    for item in shopping_list.split(","):
        temp_list.append(item)
    for i in temp_list:
        temp_ingred = i.split(" - ")[0]
        temp_ingred = temp_ingred.strip()

        for ingredient_list, breakout_list in zip(ingredient_list_types, brokenout_lists):
            if temp_ingred in ingredient_list:
                breakout_list[temp_ingred] = i

        if temp_ingred not in proteins + produce + refrigerator + dry_goods + dressing + spices:
            other_list[temp_ingred] = i


    organized_list = {}
    for breakout_list, breakout_list_str in zip(brokenout_lists, brokenout_lists_str):
        list_string = ''
        for key in sorted(breakout_list):
            list_string += str(f"{breakout_list[key]}, ")
        list_string = list_string[:-2]
        organized_list[str(breakout_list_str)] = list_string

    return organized_list, menu_meal_names, menu_link, menu_image_url, menu_description
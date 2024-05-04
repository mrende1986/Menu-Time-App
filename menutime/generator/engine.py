from flask import render_template, url_for, flash, redirect, request, Blueprint
import random
from menutime import db
from menutime.models import Meal_Details, Selections

def meal_selector(user_desired_meals, desired_servings, user_id):
    fish_meals_desired = user_desired_meals[0]
    chicken_meals_desired = user_desired_meals[1]
    beef_meals_desired = user_desired_meals[2]
    salad_meals_desired = user_desired_meals[3]
    taco_meals_desired = user_desired_meals[4]
    pasta_meals_desired = user_desired_meals[5]
    vegetarian_meals_desired = user_desired_meals[6]
    fish_ids = []
    chicken_ids = []
    beef_ids = []
    salad_ids = []
    taco_ids = []
    pasta_ids = []
    vegetarian_ids = []
    this_weeks_ids = []
    # for i in db.session.query(Meal_Details.id).distinct():
    for temp_meal in db.todos_flask.find({'category': {'$exists': True}}):
        # temp_meal = db.session.query(Meal_Details).get(i['id'])
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
        elif temp_meal['category'] == 'pasta':
            pasta_ids.append(temp_meal['id'])
        elif temp_meal['category'] == 'vegetarian':
            vegetarian_ids.append(temp_meal['id'])
        else:
            pass
    
    fish_meal_id = random.sample(fish_ids, fish_meals_desired)
    chicken_meal_id = random.sample(chicken_ids, chicken_meals_desired)
    beef_meal_id = random.sample(beef_ids, beef_meals_desired)
    salad_meal_id = random.sample(salad_ids, salad_meals_desired)
    taco_meal_id = random.sample(taco_ids, taco_meals_desired)
    pasta_meal_id = random.sample(pasta_ids, pasta_meals_desired)
    vegetarian_meal_id = random.sample(vegetarian_ids, vegetarian_meals_desired)

    this_weeks_ids = fish_meal_id + chicken_meal_id + beef_meal_id + salad_meal_id + taco_meal_id + pasta_meal_id + vegetarian_meal_id
    # new_meal_list = Selections(
    #     user_id = user_id,
    #     meal_selections = user_desired_meals,
    #     meal_portions = desired_servings,
    #     meal_ids_returned = this_weeks_ids
    #     )
    db.todos_flask.insert_one({
                    "user_id": user_id,
                    "meal_selections": user_desired_meals,
                    "meal_portions": desired_servings,
                    "meal_ids_returned": this_weeks_ids
                               })
    # db.session.commit()
    return this_weeks_ids

def populate_shopping_list(this_weeks_ids, desired_servings):

    menu_meal_names = []
    menu_ingredients = []
    menu_description = []
    menu_link = []
    menu_servings = []
    menu_image_url = []

    for id in this_weeks_ids:
        # menu_obj = db.session.query(Meal_Details).get(id)
        menu_obj = db.todos_flask.find_one({'id': (id)})
        menu_meal_names.append(menu_obj['name'])
        menu_ingredients.append(menu_obj['ingredients'])
        menu_description.append(menu_obj['description'])
        menu_link.append(menu_obj['link'])
        menu_servings.append(menu_obj['servings']) 
        menu_image_url.append(menu_obj['image_url'])

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
    proteins = ['Chicken Cutlets','Ground Beef', 'Shrimp', 'Salmon']
    produce = ['Eggplant','Avocado', 'Cilantro', 'Parsley', 'Lemon','Lime', 'Cucumber', 'Carrots', 'Garlic','Onion','Red Onion','Romaine','Tomatoes','Celery','Jalapeno','Cherry Tomatoes','Red Bell Pepper','Mango','Orange Bell Pepper','Pineapple Slices','Grape Tomatoes','Green Onions','Strawberries','Mixed Greens','Shredded Cabbage', 'Spinach','Basil', 'Green Bell Pepper']
    refrigerator = ['Egg','Feta Cheese','Butter','Sharp Cheddar Cheese','Greek Yogurt','Heavy Cream', 'Parmesan Cheese', 'Mexican Cheese','Mozzarella Cheese']
    dry_goods = ['Bow tie pasta','Breadcrumbs','Green Olives','Orzo','Brown Rice','Chili Garilc Sauce','Soy Sauce','Sweet Corn (can)','Black Beans (can)','Corn Chips (small bag)','Minced Garlic','Quinoa','Chickpeas (can(s))','Kalamata Olives','Chopped Pecans','Almonds','Sesame Seeds','Ground Ginger','Corn Tortillas', 'Nacho Doritos', 'Taco Seasoning']
    dressing = ['Marinara Sauce','Pesto','Balsamic Vinegar','Avocado Oil','White Wine Vinegar','Rice Vinegar','Low Sodium Soy Sauce','Toasted Sesame Oil','Olive Oil','Sesame Oil','Franks Red Hot Saunce',
    'Vegetable Broth','White wine vinegar','Mayonnaise','Sriracha','Honey', 'Chili Garlic Sauce','Rice Wine Vinegar','BBQ Sauce','Ranch Dressing','Maple Syrup','Apple Cider Vinegar','Canola Oil']
    frozen = ['Naan']
    spices = ['Granulated Sugar','Salt','Seasame Seeds','Dark Chili Powder','Smoked Paprika','Red Pepper Flakes','Oregano','Garlic Powder','Pepper','Cumin','Chili Powder','Coriander','Cayenne Pepper']
    other = []
    ingredient_list_types = [proteins, produce, refrigerator, dry_goods, dressing, frozen, spices, other]
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

        if temp_ingred not in proteins + produce + refrigerator + dry_goods + dressing + frozen + spices:
            other_list[temp_ingred] = i


    organized_list = {}
    for breakout_list, breakout_list_str in zip(brokenout_lists, brokenout_lists_str):
        list_string = ''
        for key in sorted(breakout_list):
            list_string += str(f"{breakout_list[key]}, ")
        list_string = list_string[:-2]
        organized_list[str(breakout_list_str)] = list_string

    return organized_list, menu_meal_names, menu_link, menu_image_url, menu_description
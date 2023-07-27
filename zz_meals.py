new_meal1 = Meal_Details(id=1, 
    name="Shrimp Tacos with Avocado Salsa Verde", 
    category="taco", 
    ingredients= ['Shrimp - 1 - pound(s)', 'Red Onion - .5 - unit(s)', 'Jalapeno - 1 - unit(s)', 'Tomatillos - 6 - unit(s)', 'Avocado - .5 - unit(s)', 'Cilantro - .25 - cup(s)', 'Lime - .5 - unit(s)', 'Garlic Powder - .25 - tsp', 'Salt - 1 - tsp', 'Pepper - 1 - tsp', 'Olive Oil - .2 - cup(s)', 'Cumin - 1 - tsp', 'Chili Powder - .5 - tsp', 'Corn Tortillas - 8 - unit(s)'],
    link = 'https://reciperunner.com/shrimp-tacos-with-avocado-salsa-verde/',
    description = "Shrimp Tacos with Avocado Salsa Verde make for an easy and healthy Mexican dinner! Pan seared shrimp topped with the most addictive salsa you’ll ever eat and all on the table in 30 minutes!",
    servings = 4,
    image_url = 'https://reciperunner.com/wp-content/uploads/2018/03/Shrimp-Tacos-Avocado-Salsa-Verde-Photograph.jpg')

db.session.add(new_meal1)
db.session.commit()

new_meal2 = Meal_Details(id=2, 
    name="Pan Seared Salmon", 
    category="fish", 
    ingredients= ['Salmon - 4 - filet(s)', 'Olive Oil - .04 - cup(s)', 'Butter - 3 - tbsp', 'Minced Garlic - 1.5 - tsp', 'Lemon - 1 - unit(s)', 'Salt - 1 - tsp', 'Pepper - 1 - tsp', 'Parsley - .2 - tbsp'],
    link = 'https://www.dinneratthezoo.com/pan-seared-salmon/',
    description = "This pan seared salmon is tender salmon fillets coated in the most delicious garlic butter sauce. A super easy dinner option that can be on the table in less than 20 minutes!",
    servings = 4,
    image_url = 'https://www.dinneratthezoo.com/wp-content/uploads/2019/04/pan-seared-salmon-3.jpg')

db.session.add(new_meal2)
db.session.commit()

new_meal3 = Meal_Details(id=3, 
    name="Spicy Salmon Bowl", 
    category="fish", 
    ingredients= ['Salmon - 4 - filet(s)', 'Avocado - 1 - unit(s)', 'Carrots - 1 - unit(s)', 'Cilantro - .25 - cup(s)', 'Garlic - 4 - clove(s)', 'Lime - 1 - unit(s)', 'Cucumber - .5 - unit(s)', 'Red Onion - .5 - unit(s)', 'Chili Garilc Sauce - .25 - cup(s)', 'Honey - 2 - tbsp', 'Mayonnaise - .5 - cup(s)', 'Soy Sauce - .33 - cup(s)', 'Sriracha - 2 - tbps', 'Brown Rice - 1 - cup(s)', 'Granulated Sugar - 1 - tbsp', 'Salt - 1 - tsp', 'Seasame Seeds - 1 - unit(s)', 'Olive Oil - .33 - cup(s)', 'Rice Wine Vinegar - .5 - cup(s)', 'Sesame Oil - 4 - tsp'],
    link = 'https://www.delish.com/cooking/recipe-ideas/a26950912/spicy-salmon-bowl-recipe/',
    description = "There is something magical about grain bowls. They are perfect for meal prepping and packing up for lunches. All of the components are great on their own, and once they're tossed together, they somehow become even better. This spicy salmon bowl has all of our favorite things.",
    servings = 4,
    image_url = 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/190326-spicy-salmon-bowl-horizontal-1556024100.png?crop=0.617xw:0.926xh;0.0527xw,0.0332xh&resize=768:*')

db.session.add(new_meal3)
db.session.commit()


new_meal4 = Meal_Details(id=4, 
    name="Southwestern Chopped Salad with Cilantro-Lime Dressing", 
    category="salad", 
    ingredients= ['Avocado - .5 - unit(s)', 'Orange Bell Pepper - 1 - unit(s)', 'Black Beans (can) - 15 - oz', 'Sweet Corn (can) - 2 - cup(s)', 'Cherry Tomatoes - 10 - oz', 'Cilantro - 1 - cup(s)', 'Garlic - 1 - clove(s)', 'Green Onions - 1 - cup(s)', 'Romaine - 1 - head(s)', 'Lime - 1 - unit(s)', 'Olive Oil - 3 - tbsp', 'White wine vinegar - 1.5 - tsp', 'Salt - 1 - tsp'],
    link = 'https://www.thegardengrazer.com/southwestern-chopped-salad-with/',
    description = "There is something magical about grain bowls. They are perfect for meal prepping and packing up for lunches. All of the components are great on their own, and once they're tossed together, they somehow become even better. This spicy salmon bowl has all of our favorite things.",
    servings = 4,
    image_url = 'https://www.thegardengrazer.com/wp-content/uploads/2013/04/southwest-chopped-salad-75-1.jpg')

db.session.add(new_meal4)
db.session.commit()


new_meal5 = Meal_Details(id=5, 
    name="Fiesta Mango Quinoa Salad", 
    category="salad", 
    ingredients= ['Avocado - .5 - unit(s)', 'Red Bell Pepper - 1 - unit(s)', 'Black Beans (can) - 15 - oz', 'Sweet Corn (can) - 1 - cup(s)', 'Mango - 1 - unit(s)', 'Cilantro - .33 - cup(s)', 'Jalapeno - 1 - unit(s)', 'Red Onion - 1 - unit(s)', 'Vegetable Broth - 2 - cup(s)', 'Lime - 1 - unit(s)', 'Olive Oil - 3 - tbsp' , 'White wine vinegar - 1.5 - tsp', 'Salt - 1 - tsp', 'Chili Powder - 2 - tsp', 'Cumin - .5 - tsp', 'Quinoa - 1 - cup(s)', 'Honey - 2 - tsp'],
    link = 'https://dishingouthealth.com/fiesta-mango-quinoa-salad/?utm_medium=social&utm_source=pinterest&utm_campaign=tailwind_tribes&utm_content=tribes&utm_term=1074714052_51191562_465382',
    description = "This quinoa salad with black beans has been one of my go-to’s for YEARS. It’s always a hit at potlucks and cookouts, and well-suited for make-ahead lunches. I mean, what’s NOT to love about a riot of texture and flavor in a 20 minute salad?",
    servings = 4,
    image_url = 'https://dishingouthealth.com/wp-content/uploads/2020/05/QuinoaSaladFinal2.jpg')

db.session.add(new_meal5)
db.session.commit()

new_meal6 = Meal_Details(id=6, 
    name="Spicy Shrimp Tacos with Avocado Crema", 
    category="taco", 
    ingredients= ['Shrimp - 1 - pound(s)', 'Avocado - 1 - unit(s)', 'Dark Chili Powder - 1 - tsp', 'Smoked Paprika - 1 - tsp', 'Minced Garlic - 1 - tsp', 'Red Pepper Flakes - .5 - tsp', 'Cilantro - .33 - cup(s)', 'Jalapeno - 1 - unit(s)', 'Garlic - 3 - clove(s)', 'Greek Yogurt - .5 - cup(s)', 'Lime - 2 - unit(s)', 'Avocado Oil - 6 - tbsp', 'White wine vinegar - 1.5 - tsp', 'Salt - 1 - tsp', 'Cumin - .5 - tsp', 'Oregano - .5 - tsp', 'Shredded Cabbage - 2 - cup(s)', 'Corn Tortillas - 8 - unit(s)'],
    link = 'https://girlwiththeironcast.com/spicy-shrimp-tacos-avocado-crema/?utm_medium=social&utm_source=pinterest&utm_campaign=tailwind_tribes&utm_content=tribes&utm_term=724445526_27932742_320',
    description = "This spicy shrimp taco recipe is everything you’ve ever wanted in a taco. Marinated shrimp topped with a homemade avocado crema recipe and delicious cabbage slaw… are you drooling yet? These are the best shrimp tacos you’ll ever eat, and a must-make every taco Tuesday!",
    servings = 4,
    image_url = 'https://girlwiththeironcast.com/wp-content/uploads/2019/05/118A2132-2-683x1024.jpg')

db.session.add(new_meal6)
db.session.commit()

new_meal7 = Meal_Details(id=7, 
    name="BBQ Chicken Salad", 
    category="salad", 
    ingredients= ['Chicken Cutlets - 1 - pound(s)', 'Sweet Corn (can) - 1 - cup(s)', 'BBQ Sauce - 1 - cup(s)', 'Ranch Dressing - 1 - cup(s)', 'Cherry Tomatoes - 10 - oz', 'Black Beans (can) - 15 - oz', 'Cilantro - 1 - cup(s)', 'Sharp Cheddar Cheese - 4 - oz', 'Red Onion - .5 - unit(s)', 'Corn Chips (small bag) - 1 - unit(s)'],
    link = 'https://www.afamilyfeast.com/bbq-chicken-salad/',
    description = "This BBQ Chicken Salad has crispy lettuce topped with tender, BBQ grilled chicken, grilled corn, black beans, shredded cheese and more!",
    servings = 8,
    image_url = 'https://www.afamilyfeast.com/wp-content/uploads/2019/05/BBQ-Chicken-Salad-4-730x1095.jpg')

db.session.add(new_meal7)
db.session.commit()

new_meal8 = Meal_Details(id=8, 
    name="Strawberry Spinach Salad", 
    category="salad", 
    ingredients= ['Chicken Cutlets - 1 - pound(s)', 'Mixed Greens - 16 - oz', 'Strawberries - 16 - oz', 'Feta Cheese - .5 - cup(s)', 'Chopped Pecans - .5 - cup(s)', 'Olive Oil - .5 - cup(s)', 'Balsamic Vinegar - .33 - cup(s)', 'Maple Syrup - 2 - tsp'],
    link = 'https://wonkywonderful.com/strawberry-spinach-salad-recipe/',
    description = "This Strawberry Spinach Salad with Homemade Balsamic Vinaigrette Dressing comes together in no time for a fresh and flavorful side salad or light dinner.",
    servings = 4,
    image_url = 'https://i0.wp.com/wonkywonderful.com/wp-content/uploads/2019/06/spinach-strawberry-salad-2.jpg?resize=985%2C1477&ssl=1')

db.session.add(new_meal8)
db.session.commit()

new_meal9 = Meal_Details(id=9, 
    name="Sriracha Lime Chicken Chopped Salad", 
    category="salad", 
    ingredients= ['Chicken Cutlets - 1 - pound(s)', 'Romaine - 4 - cup(s)', 'Pineapple Slices - 8 - slice(s)', 'Grape Tomatoes - 10 - oz', 'Red Onion - .33 - unit(s)', 'Avocado - 1 - unit(s)', 'Honey - 2 - tsp', 'Apple Cider Vinegar - .25 - cup(s)', 'Olive Oil - .33 - cup(s)', 'Lime - 3 - unit(s)', 'Sriracha - 3 - tbsp'],
    link = 'https://lexiscleankitchen.com/sriracha-lime-chicken-chopped-salad/',
    description = "This Sriracha Lime Grilled Chicken Salad is bursting with flavor. Spicy grilled chicken, sweet and juicy grilled pineapple, crisp lettuce, tomatoes, avocado, and a sweet and tangy lime vinaigrette.",
    servings = 4,
    image_url = 'https://lexiscleankitchen.com/wp-content/uploads/2014/07/Sriracha-Lime-Chicken-Salad7.jpg')


db.session.add(new_meal9)
db.session.commit()


new_meal10 = Meal_Details(id=10, 
    name="Buffalo Chicken Avocado Salad", 
    category="salad", 
    ingredients= ['Chicken Cutlets - 1 - pound(s)', 'Romaine - 3 - cup(s)', 'Tomatoes - 3 - unit(s)', 'Red Onion - .5 - unit(s)', 'Avocado - 1 - unit(s)', 'Carrots - 3 - stalk(s)', 'Celery - 3 - stalk(s)', 'Franks Red Hot Saunce - .5 - cup(s)', 'Butter - 2 - tbsp', 'Garlic Powder - .75 - tsp'],
    link = 'https://moderncrumb.com/buffalo-chicken-avocado-salad/',
    description = "The most amazing buffalo chicken avocado salad recipe. Loaded with carrots, celery, tomatoes and red onion. Spicy from the buffalo chicken but cool from the crispy lettuce and vegetables. You will be hooked on this salad!",
    servings = 4,
    image_url = 'https://moderncrumb.com/wp-content/uploads/2020/02/buffalo-chicken-avocado-salad-6-770x1024.jpg')


db.session.add(new_meal10)
db.session.commit()


new_meal11 = Meal_Details(id=11, 
    name="Mediterranean Chickpea and Feta Salad", 
    category="salad", 
    ingredients= ['Chicken Cutlets - 1 - pound(s)', 'Chickpeas (can(s)) - 30 - oz', 'Cherry Tomatoes - 16 - oz', 'Red Onion - .25 - unit(s)', 'Orange Bell Pepper - 1 - unit(s)', 'Kalamata Olives - .5 - cup(s)', 'Olive Oil - .5 - cup(s)', 'White Wine Vinegar - .25 - cup(s)', 'Lemon - 1 - unit(s)', 'Feta Cheese - .5 - cup(s)', 'Parsley - 1 - tbsp'],
    link = 'https://happilyunprocessed.com/mediterranean-chickpea-feta-salad/',
    description = "This Mediterranean Chickpea & Feta Salad is packed with all the glorious ripe veggies of summer… crisp bell peppers, cucumbers, red tomatoes, and red onion. It’s all combined with some Kalamata olives, feta cheese, and chickpeas in a lemon vinaigrette.",
    servings = 4,
    image_url = 'https://happilyunprocessed.com/wp-content/uploads/2018/07/Mediterranean-Chickpea-and-Feta-Salad-recipe-683x1024.jpg')


db.session.add(new_meal11)
db.session.commit()


new_meal12 = Meal_Details(id=12, 
    name="Sesame Chicken Salad", 
    category="salad", 
    ingredients= ['Chicken Cutlets - 1 - pound(s)', 'Shredded Cabbage - 7 - cup(s)', 'Cilantro - 1 - cup(s)', 'Green Onions - .66 - cup(s)', 'Almonds - .66 - cup(s)', 'Carrots - 2 - stalk(s)', 'Avocado - 1 - unit(s)', 'Sesame Seeds - 1 - tbs', 'Avocado Oil - 2 - tbsp', 'Rice Vinegar - 2 - tbsp', 'Low Sodium Soy Sauce - 1 - tbsp', 'Maple Syrup - 1 - tbsp', 'Toasted Sesame Oil - 1 - tsp', 'Ground Ginger - .5 - tbs', 'Minced Garlic - .25 - tbs'],
    link = 'https://www.gimmesomeoven.com/sesame-chicken-salad/',
    description = "This Sesame Chicken Salad recipe is perfectly crunchy, creamy, sweet, savory, and tossed with a yummy sesame vinaigrette.",
    servings = 5,
    image_url = 'https://www.gimmesomeoven.com/wp-content/uploads/2020/05/Sesame-Chicken-Salad-Recipe-7.jpg')

db.session.add(new_meal12)
db.session.commit()

new_meal13 = Meal_Details(id=13, 
    name="Mediterranean Orzo Salad", 
    category="salad", 
    ingredients= ['Chicken Cutlets - .5 - pound(s)', 'Orzo - 16 - oz', 'Spinach - 3 - cup(s)', 'Red Bell Pepper - 1.5 - unit(s)', 'Cucumber - 1 - unit(s)', 'Red Onion - .5 - unit(s)', 'Green Olives - 5 - oz', 'Kalamata Olives - .33 - cup(s)', 'Feta Cheese - .5 - cup(s)', 'Canola Oil - .5 - cup(s)', 'Olive Oil - .25 - cup(s)', 'Lemon - 1 - unit(s)', 'Oregano - 1.5 - tsp'],
    link = 'https://www.foodiecrush.com/mediterranean-orzo-salad/',
    description = "This vegetarian Mediterranean orzo pasta salad with crunchy vegetables and spinach, briny olives, and feta cheese makes a healthy, easy-to-make, meal-prepped meal or flavorful pasta salad side.",
    servings = 12,
    image_url = 'https://www.foodiecrush.com/wp-content/uploads/2020/02/Mediterranean-Orzo-Salad-foodiecrush.com-004-683x1024.jpg')

db.session.add(new_meal13)
db.session.commit()

new_meal14 = Meal_Details(id=14, 
    name="Avocado Salad with Tomatoes, Mozzarella, Basil Pesto", 
    category="salad", 
    ingredients= ['Chicken Cutlets - .5 - pound(s)', 'Cherry Tomatoes - 16 - oz', 'Avocado - 2 - unit(s)', 'Cucumber - 1 - unit(s)', 'Red Onion - .33 - unit(s)', 'Mozzarella Cheese - 8 - oz', 'Pesto - .25 - cup(s)', 'Lemon - 1 - unit(s)'],
    link = 'https://juliasalbum.com/avocado-salad-tomatoes-mozzarella-basil-pesto/',
    description = "Avocado Salad with Tomatoes, Mozzarella, and Basil Pesto - healthy recipe packed with nutrients and lots of fresh ingredients!  Perfect Spring and Summer salad!   Small fresh Mozzarella cheese balls are delicious when combined with avocado in this easy salad that also features red and yellow cherry tomatoes, cucumbers, and red onions.  The dressing for this avocado salad couldn't be easier to make - just combine fresh basil pesto with lemon juice!  Basil pesto makes a perfect salad dressing as it is packed with olive oil.",
    servings = 6,
    image_url = 'https://juliasalbum.com/wp-content/uploads/2018/05/Avocado-Salad-with-Tomatoes-Mozzarella-Basil-Pesto-3.jpg')

db.session.add(new_meal14)
db.session.commit()

new_meal15 = Meal_Details(id=15, 
    name="Doritos Taco Salad", 
    category="salad", 
    ingredients= ['Ground Beef - 1 - pound(s)',  'Sweet Corn (can) - 1 - cup(s)', 'Ranch Dressing - .25 - cup(s)', 'Cherry Tomatoes - 16 - oz', 'Black Beans (can) - 15 - oz', 'Green Bell Pepper - .5 - unit(s)', 'Romaine - .75 - unit(s)', 'Kalamata Olives - 8 - oz', 'Mexican Cheese - 16 - oz', 'Nacho Doritos - 2 - cup(s)', 'Taco Seasoning - 1 - unit(s)'],
    link = 'https://www.smalltownwoman.com/doritos-taco-salad/',
    description = "A fun and easy taco salad with seasoned ground beef, black olives, tomatoes, corn, black beans, a healthy helping of cheese and Doritos Tortilla Chips all tossed in a homemade Catalina Salad Dressing.",
    servings = 6,
    image_url = 'https://www.smalltownwoman.com/wp-content/uploads/2020/02/Doritos-Taco-Salad-II-11.webp')

db.session.add(new_meal15)
db.session.commit()

new_meal16 = Meal_Details(id=16, 
    name="Tuscan Butter Salmon", 
    category="fish", 
    ingredients= ['Salmon - 4 - filet(s)',  'Olive Oil - .04 - cup(s)', 'Butter - 3 - tbsp', 'Cherry Tomatoes - 24 - oz', 'Garlic - 8 - oz', 'Spinach - 2 - cup(s)', 'Heavy Cream - .5 - cup(s)', 'Parmesan Cheese - 8 - oz', 'Basil - 4 - oz', 'Lemon - 1 - unit(s)'],
    link = 'https://thefoodcharlatan.com/creamy-tuscan-salmon/',
    description = "This Creamy Tuscan Salmon recipe is totally restaurant quality, but super easy to make! Perfectly pan-seared salmon, drowning in a creamy parmesan sauce with garlic, cherry tomatoes, spinach, and fresh basil. It’s the perfect summer meal and is done in 30 minutes!",
    servings = 4,
    image_url = 'https://thefoodcharlatan.com/wp-content/uploads/2020/05/Creamy-Tuscan-Salmon-30-Minute-Dinner-5-650x975.jpg')

db.session.add(new_meal16)
db.session.commit()

new_meal17 = Meal_Details(id=17, 
    name="Italian Chopped Salad", 
    category="salad", 
    ingredients= ['Salami - .5 - pound(s)', 'Cherry Tomatoes - 12 - oz', 'Pepperoncini Rings - .5 - cup(s)', 'Red Onion - .5 - unit(s)', 'Romaine - 2 - cup(s)', 'Kalamata Olives - 8 - oz', 'Italian Vinaigrette - 1 - cup(s)', 'Provolone Cheese - .5 - pound(s)'],
    link = 'https://www.afarmgirlsdabbles.com/italian-chopped-salad/',
    description = "Italian Chopped Salad from afarmgirlsdabbles.com - an Italian salad loaded with fresh goodness, plus salami, provolone, pepperoncini, and olives. It's light, yet hearty, and extra flavorful with a zippy Italian vinaigrette!",
    servings = 8,
    image_url = 'https://www.afarmgirlsdabbles.com/wp-content/uploads/2019/07/Italian-chopped-salad_AFarmgirlsDabbles_AFD-4-b2-600x900.jpg')

db.session.add(new_meal17)
db.session.commit()

new_meal18 = Meal_Details(id=18, 
    name="Damn Good Salmon Taco Bowls", 
    category="fish", 
    ingredients= ['Salmon - 2 - filet(s)', 'Avocado - 1 - unit(s)', 'Coriander - .25 - cup(s)', 'Cilantro - .25 - cup(s)', 'Garlic - 2 - clove(s)', 'Lime - 1 - unit(s)', 'Green Bell Pepper - .25 - unit(s)', 'Green Onions - .5 - cup(s)', 'Salsa - 1 - cup(s)', 'Greek Yogurt - .25 - cup(s)', 'Rice - .75 - cup(s)', 'Tomato Sauce - .5 - cup(s)', 'Yellow Onion - .25 - cup(s)', 'Powdered Garlic - .75 - tsp', 'Cayenne Pepper - .2 - tbp', 'Chili Powder - .75 - tsp', 'Cumin - 1.25 - tsp', 'Olive Oil - .2 - cup(s)'],
    link = 'https://www.ambitiouskitchen.com/salmon-taco-bowls/',
    description = "Delicious salmon taco bowls with homemade taco seasoned salmon and served with flavorful sofrito rice. Add avocado, salsa, green onion, cilantro and any other toppings your heart desires for a wonderful meal prep dinner for two!",
    servings = 2,
    image_url = 'https://www.ambitiouskitchen.com/wp-content/uploads/2019/12/Damn-Good-Salmon-Taco-Bowls-4.jpg')

db.session.add(new_meal18)
db.session.commit()

new_meal19 = Meal_Details(id=19, 
    name="Cobb Salad", 
    category="salad", 
    ingredients= ['Chicken Cutlets - .5 - pound(s)', 'Avocado - 1 - unit(s)', 'Cherry Tomatoes - 8 - oz', 'Romaine - .75 - unit(s)', 'Eggs - 2 - unit(s)', 'Green Onions - .5 - cup(s)', 'White wine vinegar - 3 - tsp', 'Dijon mustard - 2 - tsp', 'Honey - 2 - tbsp', 'Oregano - 1 - tsp', 'Olive Oil - .2 - cup(s)'],
    link = 'https://www.deliciousmeetshealthy.com/cobb-salad-recipe/#wprm-recipe-container-10212',
    description = "This beautiful and delectable Cobb salad brings all the best hearty protein together with fresh greens, tomatoes, and avocados. Healthy summer lunch or dinner, made in less than 30 minutes",
    servings = 4,
    image_url = 'https://www.deliciousmeetshealthy.com/wp-content/uploads/2019/08/Cobb-Salad-2-680x1024.jpg.webp')

db.session.add(new_meal19)
db.session.commit()

new_meal20 = Meal_Details(id=20, 
    name="Zesty Lime Shrimp and Avocado Salad", 
    category="salad", 
    ingredients= ['Shrimp - 1 - pound(s)', 'Lime - 2 - unit(s)', 'Avocado - 1 - unit(s)', 'Cherry Tomatoes - 8 - oz', 'Jalapeno - 1 - unit(s)', 'Cilantro - .25 - cup(s)', 'Olive Oil - .2 - cup(s)'],
    link = 'https://www.skinnytaste.com/zesty-lime-shrimp-and-avocado-salad/',
    description = "Lime juice and cilantro are the key ingredients to creating this wonderful, healthy no-cook salad you'll want to make all summer long.",
    servings = 4,
    image_url = 'https://www.skinnytaste.com/wp-content/uploads/2015/06/Zesty-Lime-Shrimp-_-Avocado-Salsa-5.jpg')

db.session.add(new_meal20)
db.session.commit()

new_meal21 = Meal_Details(id=21, 
    name="Skillet Seared Salmon with Creamy Cilantro Lime Sauce", 
    category="fish", 
    ingredients= ['Salmon - 4 - filet(s)', 'Lime - 2 - unit(s)', 'Green Onions - .25 - cup(s)', 'Cilantro - .5 - cup(s)', 'Salt - 1 - tsp', 'Pepper - 1 - tsp', 'Olive Oil - .2 - cup(s)', 'Cumin - 1 - tsp', 'Coriander - .5 - tsp', 'Cayenne Pepper - .2 - tbp', 'Garlic - 2 - clove(s)'],
    link = 'https://www.cookingclassy.com/skillet-seared-salmon-with-creamy-cilantro-lime-sauce/',
    description = "Cilantro Lime Salmon is such an exciting way to make salmon! It’s boasting with so much fresh flavor and who could resist that sauce! Not to mention you can have this ready in 20 minutes, can’t beat that.",
    servings = 4,
    image_url = 'https://www.cookingclassy.com/wp-content/uploads/2017/05/skillet-seared-salmon-creamy-cilantro-lime-sauce-3-768x1152.jpg')

db.session.add(new_meal21)
db.session.commit()

new_meal22 = Meal_Details(id=22, 
    name="Cilantro Lime Pasta Salad", 
    category="pasta", 
    ingredients= ['Bow tie pasta - .5 - pound(s)', 'Sweet Corn (can) - 1.5 - cup(s)', 'Cherry Tomatoes - 24 - oz', 'Red Onion - .5 - unit(s)', 'Cilantro - .25 - cup(s)', 'Greek Yogurt - .5 - cup(s)', 'Lime - 1 - unit(s)', 'Avocado - 1.5 - unit(s)', 'Cayenne Pepper - .2 - tbp', 'Salt - 1 - tsp', 'Garlic - 2- clove(s)'],
    link = 'http://kaleforniakravings.com/cilantro-lime-pasta-salad/#recipe',
    description = "Perfect for potlucks, picnics & summer BBQ’s! This easy pasta salad is loaded with fresh corn, tomatoes, onion & cilantro all tossed in a creamy homemade cilantro lime dressing! It’s simple, refreshing & the best dish for summer!",
    servings = 6,
    image_url = 'https://i0.wp.com/kaleforniakravings.com/wp-content/uploads/2022/06/Cilantro-lime-pasta-salad-11.jpg?resize=683%2C1024')

db.session.add(new_meal22)
db.session.commit()

new_meal23 = Meal_Details(id=23, 
    name="Baked Eggplant Parmesan", 
    category="pasta", 
    ingredients= ['Butter - 3 - tbsp', 'Breadcrumbs - .5 - cup(s)', 'Parmesan Cheese - 8 - oz', 'Eggplant - 1 - unit(s)', 'Egg - 1 - unit(s)', 'Marinara Sauce - 1 - cup(s)', 'Mozzarella Cheese - 2 - oz'],
    link = 'https://www.theseasonedmom.com/baked-eggplant-parmesan/',
    description = "Grandma's easy Baked Eggplant Parmesan is a delicious vegetarian dinner with just 15 minutes of prep!",
    servings = 4,
    image_url = 'https://www.theseasonedmom.com/wp-content/uploads/2021/10/Baked-Eggplant-Parmesan-5.jpg')

db.session.add(new_meal23)
db.session.commit()

new_meal24 = Meal_Details(id=24, 
    name="Peruvian Chicken with Green Sauce", 
    category="chicken", 
    ingredients= ['Chicken Cutlets - 2 - pound(s)', 'Garlic - 7 - clove(s)', 'Low Sodium Soy Sauce - 6 - tbsp', 'Lime - 2 - unit(s)', 'Olive Oil - 5 - tbsp', 
                'Cumin - 2 - tsp', 'Paprika - 1 - tsp', 'Oregano - 0.5 - tsp', 'Black Pepper - 3 - tsp', 'Jalapeno - 3 - unit(s)', 
                'Cilantro - 1 - cup(s)', 'Green Onions - .33 - cup(s)', 'Mayonnaise - 0.5 - cup(s)', 'Greek Yogurt - .25 - cup(s)',
                'Salt - 0.5 - tsp'],
    link = 'https://www.platingsandpairings.com/peruvian-grilled-chicken-creamy-green-sauce/',
    description = "This Peruvian Chicken with Creamy Green Sauce packs in big flavors thanks to the easy marinade and vibrant green sauce (aji verde).",
    servings = 4,
    image_url = 'https://www.platingsandpairings.com/wp-content/uploads/2018/07/peruvian-chicken-recipe-11-1365x2048.jpg')

db.session.add(new_meal24)
db.session.commit()

new_meal25 = Meal_Details(id=25, 
    name="Baked Eggplant Parmesan", 
    category="vegetarian", 
    ingredients= ['Butter - 3 - tbsp', 'Breadcrumbs - .5 - cup(s)', 'Parmesan Cheese - 8 - oz', 
                'Eggplant - 1 - unit(s)', 'Egg - 1 - unit(s)', 'Marinara Sauce - 1 - cup(s)', 'Mozzarella Cheese - 2 - oz'],
    link = "https://www.theseasonedmom.com/baked-eggplant-parmesan/",
    description = "Grandma's easy Baked Eggplant Parmesan is a delicious vegetarian dinner with just 15 minutes of prep!",
    servings = 4,
    image_url = "https://www.theseasonedmom.com/wp-content/uploads/2021/10/Baked-Eggplant-Parmesan-5.jpg")

db.session.add(new_meal25)
db.session.commit()

new_meal26 = Meal_Details(id=26, 
    name="Best Lentil Soup", 
    category="vegetarian", 
    ingredients= ['Brown Lentils - 1 - cup(s)', 'Carrots - 2 - stalk(s)', 'Kale - 16 - oz', 'Garlic - 4 - clove(s)', 'Thyme - 0.5 - tsp(s)', 'Canned Tomatoes Large - 1 - unit(s)', 'Yellow Onion - 1.5 - cup(s)', 'Vegetable Broth - 4 - cup(s)', 'Lemon - 1 - unit(s)', 'Black Pepper - 3 - tsp', 'Curry Powder - 2 - tsp(s)', 'Red Pepper Flakes - 1 - tsp', 'Salt - 1 - tsp', 'Cumin - 2 - tsp', 'Olive Oil - .5 - cup(s)'],
    link = 'https://cookieandkate.com/best-lentil-soup-recipe/',
    description = "This simple vegan lentil soup recipe comes together quickly with mostly pantry ingredients. Be sure to have your ingredients prepped and ready before you start cooking! Recipe yields four large bowls of soup, or six more modest servings.",
    servings = 4,
    image_url = 'https://cookieandkate.com/images/2019/01/best-lentil-soup-recipe-4-768x1154.jpg')

db.session.add(new_meal26)
db.session.commit()

new_meal27 = Meal_Details(id=27, 
    name="Mom's Taquitos", 
    category="beef", 
    ingredients= ['Roast Beef - 24 - oz(s)', 'Yellow Onion - 1 - cup(s)', 'Vegetable Oil - 1.5 - cup(s)', 'Cumin - 2 - tsp', 'Salt - 0.5 - tsp', 'Garlic Powder - .5 - tsp', 'Corn Tortillas - 1 - package(s)'],
    link = 'https://www.pinterest.com/pin/347551296255224749/',
    description = "A family favorite!",
    servings = 4,
    image_url = 'https://i.pinimg.com/564x/06/83/0a/06830a013f44cd67ef4292f3c8f85fb9.jpg')

db.session.add(new_meal27)
db.session.commit()

new_meal28 = Meal_Details(id=28, 
    name="Chicken Marsala", 
    category="chicken", 
    ingredients= ['Chicken Cutlets - 1 - pound(s)', 'Marsala Wine - 1.25 - cup(s)', 'Chicken Broth - 1.25 - cup(s)', 'Pepper - 1 - tsp', 'Salt - 0.5 - tsp', 'Flour - .33 - cup(s)', 'Butter - 2 - tbsp', 'Olive Oil - 3 - tbsp', 'Mushrooms - 8 - oz', 'Garlic - 3 - clove(s)', 'Thyme - 1 - tsp(s)', 'Oregano - 1 - tsp', 'Cornstarch - 1.5 - tsp(s)', 'Chicken Broth - .1 - cup(s)', 'Heavy Cream - .33 - cup(s)', 'Parsley - 1 - tbsp', 'Bow tie pasta - .5 - pound(s)'],
    link = 'https://www.cookingclassy.com/chicken-marsala/',
    description = "Chicken Marsala with a creamy sauce! This classic Italian-American chicken recipe includes tender, perfectly pan seared chicken cutlets, and flavor enhancing browned mushrooms, and it’s all covered with a richly seasoned marsala wine, garlic and herb sauce. \nNote: We serve over pasta.",
    servings = 4,
    image_url = 'https://www.cookingclassy.com/wp-content/uploads/2020/02/chicken-marsala-02.jpg')

db.session.add(new_meal28)
db.session.commit()
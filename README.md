# Personalized_Recipe_Recommender
Recipe recommendation system based on user’s input (ingredients, time to cook, &amp; nutritional information).
## Background
Food is the source of energy, having food high in nutritional value is important for the overall health. Being aware of the amount of nutrients in our food help us keep track of meeting our daily needs of energy and nutrients, thus maintaining our health. Time availability to cook varies from time to time, but that shouldn’t prevent us from having the same nutritious meals. For that, I wanted to create a Recommendation system that suggest a recipe based on user’s preference of main ingredient, time to cook, and nutritional information.
## Data
Original dataset contained 35,516 instances & 47 feature. The dataset was scrapped from a recipe website called Allrecipe, and was obtained from this GitHub repo:
https://github.com/shaansubbaiah/allrecipes-scraper/tree/main/export

For this project I will be using 13 features which are:
| Feature         | Description |
|  :---:          |   :---:     |
|  name           | recipe name |
| category        | Recipe category, example (main dish, desserts, bread, world-cuisine ... ect) |
| rating          | Recipe rating |
| rating count    | Number of ratings |
| url             | link to this recipe |
| ingredients     | ingredients used in this recipe |
| total           | total recipe time, preparation and cooking time |
| servings        | number of servings in this recipe |
| yield           | what will this recipe yield, example (4 servings, 3 cups, 12 cupcakes, ... ect) |
| calories        | amount of calories per serving |
| carbohydrates_g | grams of carbohydrate per serving |
| fat_g           | grams of fat per serving |
| protein_g       | grams of protein per serving |

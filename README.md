# Personalized_Recipe_Recommender
Recipe recommendation system based on user’s input (ingredients, time to cook, &amp; nutritional information).
## Background
Food is the source of energy, having food high in nutritional value is important for the overall health. Being aware of the amount of nutrients in our food help us keep track of meeting our daily needs of energy and nutrients, thus maintaining our health. Time availability to cook varies from time to time, but that shouldn’t prevent us from having the same nutritious meals. For that, I wanted to create a Recommendation system that suggest a recipe based on user’s preference of main ingredient, time to cook, and nutritional information.
## Motivation
As someone who studied clinical nutrition and loves cooking, sometimes I don’t feel motivated to cook especially whenever I’m busy & don’t have enough time which sometimes reduces my diet quality. For that reason, I decided to create this recommendations system project that not only take into account the nutrition facts of the recipe but also the total time to cook to help me & everyone else to keep our diet quality despite of the time availability! 
## Data
Original dataset contained 35,516 instances & 47 feature. The dataset was scrapped from a recipe website called Allrecipes, and was obtained from this GitHub repo:
https://github.com/shaansubbaiah/allrecipes-scraper/tree/main/export

For this project I will be using 14 features which are:
| Feature         | Description |
|  :---:          |   :---:     |
|  name           | recipe name |
| category        | recipe category, example (main dish, desserts, bread, world-cuisine ... ect) |
| rating          | recipe rating |
| rating count    | number of ratings |
| url             | link to this recipe |
| ingredients     | ingredients used in this recipe |
| total           | total recipe time (in minutes) preparation and cooking time |
| servings        | number of servings in this recipe |
| yield           | what will this recipe yield, example (4 servings, 3 cups, 12 cupcakes, ... ect) |
| calories        | amount of calories per serving |
| carbohydrates_g | grams of carbohydrate per serving |
| fat_g           | grams of fat per serving |
| protein_g       | grams of protein per serving |

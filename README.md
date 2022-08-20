# Personalized_Recipe_Recommender
Recipe recommendation system based on user’s input (time to cook, &amp; nutritional information).
## Background
Food is the source of energy, having food high in nutritional value is important to support the overall health. Being aware of the amount of nutrients in our food help us keep track of meeting our daily needs of energy and nutrients, thus maintaining our health. The availability of time to cook can vary from time to time, but that shouldn’t prevent us from having the same nutritious meals.
## Motivation
As someone who studied clinical nutrition and loves cooking, sometimes I don’t feel motivated to cook especially whenever I’m busy & don’t have enough time which sometimes reduces my diet quality. For that reason, I decided to create this recommendations system project that not only takes into account the nutritional value of the recipe but also the total time to cook to help me & everyone else to keep our diet quality despite of the time availability!
## Data
Original dataset contained 35,516 instances & 47 feature. The dataset was scrapped on May 2021 from a recipe website called Allrecipes and was used to provide insight of the nutritional value of various recipes. Original data obtained from this GitHub repo:
https://github.com/shaansubbaiah/allrecipes-scraper/tree/main/export

For this project, after cleaning the original dataset and saving it in data file as (full_cleaned_data).
The final data shape was 19,224 instances and 14 features which are:
| Feature         | Description |
|  :---:          |   :---:     |
|  name           | recipe name |
| category        | recipe category, example (main dish, desserts, bread, world-cuisine ... ect) |
| rating          | recipe rating |
| rating count    | number of ratings |
| url             | link to this recipe |
| ingredients     | the original ingredients used in this recipe as scrapped from the website |
| total           | total recipe time (in minutes) preparation and cooking time |
| servings        | number of servings in this recipe |
| yield           | what will this recipe yield, example (4 servings, 3 cups, 12 cupcakes, ... ect) |
| calories        | amount of calories per serving |
| carbohydrates_g | grams of carbohydrate per serving |
| fat_g           | grams of fat per serving |
| protein_g       | grams of protein per serving |
| ingredients_parsed | ingredients after cleaning measurements, punctuations & common words|
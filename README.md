# Personalized_Recipe_Recommender
Recipe recommendation system based on user’s input (time to cook, &amp; nutritional information).
## Background
Food is the source of energy, having food high in nutritional value is important to support the overall health. Being aware of the amount of nutrients in our food help us keep track of meeting our daily needs of energy and nutrients, thus maintaining our health. The availability of time to cook can vary from time to time, but that shouldn’t prevent us from having the same nutritious meals.
## Motivation
As someone who studied clinical nutrition and enjoys cooking, sometimes I don’t feel motivated to cook especially whene I’m busy & don’t have enough time which sometimes reduces my diet quality. For that reason, I decided to create this recommendations system project that not only takes into account the nutritional value of the recipe but also the total time to cook to help me & everyone else to keep our diet quality despite of the time availability!
## Data
Original dataset contained 35,516 instances & 47 feature. The dataset was scrapped on May 2021 from a recipe website called Allrecipes and was used to provide insight of the nutritional value of various recipes. Original data obtained from this GitHub repo:
https://github.com/shaansubbaiah/allrecipes-scraper/tree/main/export

For this project, after cleaning the original dataset and saving it in data file as (full_cleaned_data).
The final data shape was 19,179 instances and 14 features which are:
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
## Folders
scr: Recipe.ipynb (jupyter notebook contains data cleaning & EDA)\
model: model.ipynb  (the recommending system model)\
web: app.py, requirements.txt, the_model.pkl (streamlit app but it's not working yet) \
data: full_cleaned.csv, scrapped-07-05-21.csv (cleaned & original data)\
## References
Presentation references:
1. Human energy requirements. Retrieved 23 August 2022, from https://www.fao.org/3/y5686e/y5686e04.htm
2. Subbaiah, S. (2021). GitHub - shaansubbaiah/allrecipes-scraper: 🥗 Scrapy spider to scrape recipe and nutritional data from allrecipes.com. Retrieved 23 August 2022, from https://github.com/shaansubbaiah/allrecipes-scraper
3. ML - Content Based Recommender System - GeeksforGeeks. (2020). Retrieved 23 August 2022, from https://www.geeksforgeeks.org/ml-content-based-recommender-system/
4. Shimodaira, H. (2015). Similarity and recommender systems. Retrieved 23 August 2022, from https://www.inf.ed.ac.uk/teaching/courses/inf2b/learnnotes/inf2b-learn-note02-2up.pdf
5. Cosine Similarity - GeeksforGeeks. (2020). Retrieved 23 August 2022, from https://www.geeksforgeeks.org/cosine-similarity/
6. C program to find the Euclidean distance between two points - GeeksforGeeks. (2021). Retrieved 23 August 2022, from https://www.geeksforgeeks.org/c-program-to-find-the-euclidean-distance-between-two-points/
7. COSINE DISTANCE COSINE SIMILARITY ANGULAR COSINE DISTANCE ANGULAR COSINE SIMILARITY. (2017). Retrieved 23 August 2022, from https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/cosdist.htm
Codes function used/guidance references:
https://stackoverflow.com/questions/35970760/convert-1h30min-string-to-minutes-in-python 
https://github.com/jackmleitch/whatscooking-deployment
https://www.kaggle.com/code/yyzz1010/content-based-filtering-recipe-recommender 
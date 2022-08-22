import streamlit as st
import pandas as pd
import joblib
header = st.beta_container()
recommendation_system = st.beta_container()
##read the data
recipes = pd.read_csv('../data/full_clean_data.csv')

with header:
    st.title('Welcome to Personalized Recipy Recommendation!!')
    
with recommendation_system:
    st.header('Please customize your inpur below')
    a = st.slider('How much time you have to cook?', 1, 1440)
    b = st.slider('How many calories per serving do you prefer?', 4, 873)
    c = st.slider('How many grams of carbohydrate per serving do you prefer?', 0, 123)
    d = st.slider('How many grams of fat per serving do you prefer?', 0, 28)
    e = st.slider('How many grams of protein per serving do you prefer?', 0, 63)
    ##click done/recommend
    if st.button('Recommend Recipies Please :)'):
        #unpack the recommendation function
        model = joblib.load('model.pkl')
        #get recommendation
        recommend = model.predict(a, b, c, d, e)[0]
        # Output recommendation
        st.text(f"This instance is a {recommend}")
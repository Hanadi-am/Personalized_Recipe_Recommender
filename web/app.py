# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import streamlit as st
import joblib
header = st.beta_container()
recommendation_system = st.beta_container()
with header:
    st.title('Welcome to Personalized Recipy Recommendation!!')
with recommendation_system:
    st.header('Please customize your inpur below')
    a = st.slider('How much time you have to cook?', 1, 1440)
    b = st.slider('How many calories per serving do you prefer?', 4, 873)
    c = st.slider('How many grams of carbohydrate per serving do you prefer?', 0, 123)
    d = st.slider('How many grams of fat per serving do you prefer?', 0, 28)
    e = st.slider('How many grams of protein per serving do you prefer?', 0, 63)
    ##click the recommend button
    if st.button('Recommend Recipies Please :)'):
        #unpack the recommendation function
        model = joblib.load('the_model.pkl')
        #get recommendation
        recommend = model.predict(a, b, c, d, e)[0]
        # Output recommendation
        st.text(f"This instance is a {recommend}")
        
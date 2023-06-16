import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header(' Breakfast Menu')

streamlit.text('🥣 omega 3 & blueberry outmeal')

streamlit.text('🥗 Kale Spinach & Rocket Smothie')

streamlit.text('🐔 Hard boiled Free-range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

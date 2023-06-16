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
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),["Avocado","Strawberries"])

# Display the table on the page.

streamlit.dataframe(my_fruit_list)

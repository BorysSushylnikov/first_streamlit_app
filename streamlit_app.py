import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#create the repeatable code block (called a function)
def get_fuityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  # take the json version of the response and normalize it
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

streamlit.title("My Parents New Healthy Dinner")
streamlit.header("Breakfast Menu")

streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Ricket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Insert a pick list so to choose what fruits they want to include.

fruit_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruits_to_show)

# New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruit_choice = streamlit.text:input("What fruit would you like information about?")
      if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
      else:
        back_from_function = get_fuityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
 
except URLError as e:
  streamlit.error()
      
streamlit.write('The user entered', fruit_choice)
# streamlit.text(fruityvice_response.json()) # just writes the data to the screen 


streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values('from streamlit')")
my_data_rows = my_cur.fetchall()

streamlit.header("My fruit load list contains:")
streamlit.dataframe(my_data_rows)

# New Section to display fruityvice api response pt 2
fruit_choice1 = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
fruityvice_response1 = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice1)
# streamlit.text(fruityvice_response1.json()) # just writes the data to the screen 
streamlit.text("Thanks for adding " + fruit_choice1)




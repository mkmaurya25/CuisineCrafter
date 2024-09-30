import streamlit as st
import helper_v2

st.title("CuisineCrafter: Restaurant Name & Menu Designer")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    # Get the response from helper_v2
    response = helper_v2.generate_restaurant_name_and_items(cuisine)
    
    # Display the restaurant name
    st.header(response['name'].content)
    
    # Access menu from response, and split it into individual items
    menu_items = response['menu'].content.split(', ')
    
    # Display the menu items
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

import streamlit as st
import helper
# import helper_v2


st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    response = helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)


# import streamlit as st
# import helper

# st.title("Restaurant Name Generator")

# cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

# if cuisine:
#     # Simply call the function without invoking again
#     response = helper.generate_restaurant_name_and_items(cuisine)
    
#     st.write("Response:", response)  # Debugging output to check the structure
    
#     # Assuming the response is a dictionary
#     if isinstance(response, dict):
#         st.header(response['restaurant_name'].strip())
#         menu_items = response['menu_items'].strip().split(",")
#         st.write("**Menu Items**")
#         for item in menu_items:
#             st.write("-", item)
#     else:
#         st.error("Unexpected response format. Please check the helper function.")


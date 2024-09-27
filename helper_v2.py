# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableMap
# from langchain_groq import ChatGroq
# from secret import groq_api_key

# import os
# os.environ['GROQ_API_KEY'] = groq_api_key

# llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)

# def generate_restaurant_name_and_items(cuisine):
    
#     name_chain = (
#         ChatPromptTemplate.from_template(
#             "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
#         ) | llm
#     )
    
#     menu_chain = (
#         ChatPromptTemplate.from_template(
#             "Suggest some menu items for {restaurant_name}. Return it as a comma separated string"
#         ) | llm
#     )

#     # Run the name_chain first, then use its output as input for the menu_chain
#     # chain = RunnableMap({
#     #     'name': name_chain,
#     #     'menu': menu_chain
#     # })
#     response = RunnableParallel(name=name_chain, menu=menu_chain)

#     # return chain.stream({'cuisine': cuisine})
#     return response.invoke({'cuisine': cuisine, 'restaurant_name': cuisine})


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_groq import ChatGroq
from secret import groq_api_key

import os
os.environ['GROQ_API_KEY'] = groq_api_key

# Initialize the LLM
llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Step 1: Generate the restaurant name
    name_chain = (
        ChatPromptTemplate.from_template(
            "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
        ) | llm
    )
    
    # Step 2: Generate the menu items
    menu_chain = (
        ChatPromptTemplate.from_template(
            "Suggest some menu items for {restaurant_name}. Return it as a comma separated string."
        ) | llm
    )
    
    # Combine chains into a parallel runnable
    response = RunnableParallel(name=name_chain, menu=menu_chain)

    # Invoke with both cuisine and restaurant_name
    result = response.invoke({
        'cuisine': cuisine, 
        'restaurant_name': cuisine  # The actual restaurant name will come from the output of name_chain
    })

    # Return the response dictionary
    return result

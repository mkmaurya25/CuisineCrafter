---
layout: default
title: "Cusine Crafter"
---

<!--<style>
.page-header .btn.github-repo,
.page-header .btn.github-repo a {
    display: none !important;
    visibility: hidden !important;
    pointer-events: none !important;
    opacity: 0 !important;
}
</style>-->

# CuisineCrafter: A Generative AI Tool for Culinary Inspiration

**CuisineCrafter** is an innovative generative AI-based application designed to create imaginative and culturally relevant restaurant names and menu options. Powered by the LangChain framework and ChatGroq models, CuisineCrafter provides a unique experience for restaurateurs, entrepreneurs, and food enthusiasts looking for culinary inspiration across various cuisines.

![CuisineCrafter Interface](assets/images/output.gif) <!-- Adjust path accordingly -->


## Overview

CuisineCrafter is a user-friendly app that leverages the power of AI to instantly generate restaurant names and themed menu items based on a selected cuisine. Whether you are starting a new restaurant or simply seeking inspiration for your culinary projects, CuisineCrafter is your go-to tool for creativity in the culinary industry.

### Key Features
- **Creative Restaurant Names**: Generates unique, cuisine-specific names for your restaurant.
- **Curated Menu Suggestions**: Provides a list of relevant and imaginative menu items based on the generated restaurant name.
- **Diverse Cuisine Support**: Supports multiple cuisines, including Indian, Italian, Mexican, Arabic, and American.
- **Interactive User Interface**: Built with Streamlit, offering a seamless and engaging user experience.

## Installation Guide

To set up CuisineCrafter locally on your machine, follow these simple steps:

### Installation
To set up CuisineCrafter locally, follow these steps:

1. Clone the repository:
```
git clone https://github.com/your-username/cuisinecrafter.git
cd cuisinecrafter
```
2. Install the dependencies
```
pip install -r requirements.txt
```

3. Set up your Groq API key:
```
export GROQ_API_KEY="your_groq_api_key"
```

4. Run the app:
```
streamlit run app.py
```
## Usage Instructions

Once the app is running, you can easily generate restaurant names and menu items:
1. Launch the App: Execute the command streamlit run app.py in your terminal.
2. Select a Cuisine: Use the sidebar dropdown to choose a cuisine (e.g., Indian, Italian, Mexican).
3. View Generated Content: The app will display a creative restaurant name along with a curated list of menu items based on your selection.

## Customization Options

If you want to personalize the CuisineCrafter experience, you can modify the application in the following ways:
1. **Adding New Cuisines:** Extend the list of supported cuisines by editing the app.py file.
2. **Modifying Prompts:** Update the prompts inside helper_v2.py to change how names and menus are generated, tailoring the output to fit your needs.

## Tech Stack

CuisineCrafter is built with the following technologies:
1. LangChain: Integrates with the Groq LLM model for powerful language generation.
2. Streamlit: Provides a dynamic and interactive frontend for user engagement.
3. Groq API: Utilized for accessing and leveraging the LLM capabilities to generate creative responses.

## Conclusion
CuisineCrafter stands as a testament to the potential of generative AI in the culinary industry, allowing users to explore unique restaurant concepts and menu items effortlessly. Whether you're an aspiring restaurateur or a culinary enthusiast, this tool can provide you with the inspiration needed to make your culinary vision a reality.

Feel free to explore the repository and start crafting your culinary ideas with CuisineCrafter!

```python
if process_url_clicked:
    # Load data from URLs
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    # Split data into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    docs = text_splitter.split_documents(data)
```

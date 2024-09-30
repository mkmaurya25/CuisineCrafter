# CuisineCrafter

**CuisineCrafter** is an generative AI-based tool designed to generate creative, cuisine-specific restaurant names and menu options. Powered by the LangChain framework and ChatGroq models, CuisineCrafter delivers imaginative and culturally relevant names and food offerings for various restaurant themes.

### Overview

CuisineCrafter is a user-friendly app that harnesses the power of AI to generate restaurant names and menus based on a selected cuisine. With the ability to instantly create themed names and curated menu items, CuisineCrafter is perfect for restaurateurs, entrepreneurs, and food enthusiasts looking for inspiration in the culinary industry.

### Features
- Generates creative, cuisine-specific restaurant names.
- Suggests menu items for the generated restaurant names.
- Supports multiple cuisines: Indian, Italian, Mexican, Arabic, and American.
- Built with LangChain’s LLM integration and Streamlit for an interactive UI.

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

### Usage
- Launch the app using the streamlit run app.py command.
- Choose a cuisine from the sidebar dropdown (e.g., Indian, Italian, Mexican).
- The app will generate a creative restaurant name and a list of curated menu items based on the selected cuisine.
- View the results on the main page, where both the restaurant name and the menu will be displayed.

### Customization
If you'd like to modify the prompts or add more cuisines, you can customize the helper_v2.py file, where the core logic for generating restaurant names and menu items resides.

- Adding new cuisines: Extend the cuisine list in app.py.
- Modifying prompts: Update the prompts inside helper_v2.py to change how names and menus are generated.

### Tech Stack
- LangChain: To integrate with the Groq LLM model.
- Streamlit: For the app's frontend and user interaction.
- Groq API: For accessing and utilizing the LLM for generating responses.

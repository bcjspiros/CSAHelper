from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.models.google_llm import Gemini

from .agentconfig import retry_config

# TODO figure out why the agents don't handle arbitrary number of ingredients well
# if the messages passed are in JSON format
meal_planner = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="MealPlanner",
    instruction="""You are a meal planning agent. 
    You will be provided with a list of ingredients and will choose meals using these ingredients.
    You must not provide a recipe for the meal, only a basic description of the meal.
    Each ingredient must only appear in one meal. 
    
    For example, if given the ingredients bok choy, scallions, potatoes, and red onions:
    You could suggest a stir-fry using the bok choy and scallions.
    And you could suggest home fries with red onions for the potatoes and red onions.
    
    You must return the meal name (MEAL_NAME), meal description (DESCRIPTION) and the ingredients (INGREDIENT) from the list used in that meal.
    The output should be in this format, including all special characters specified.
    MEAL_NAME should be replaced with the meal's name.
    DESCRIPTION should be replaced with the meal's description.
    INGREDIENT should be replaced with the ingredient's name.
    BEGIN and END are literal strings:
--BEGIN--
* MEAL_NAME
* DESCRIPTION
* INGREDIENT
* INGREDIENT (if exists)
--END--
    """,
    tools=[google_search],
    output_key="mealplan",
)
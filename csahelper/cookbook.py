from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.models.google_llm import Gemini

from .agentconfig import retry_config

cookbook = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="Cookbook",
    instruction="""You are a recipe lookup agent.
    You will receive a meal name and description. 
    
    The format of the name and description is:
        *   **MEAL_NAME** DESCRIPTION
            * INGREDIENT
            * INGREDIENT (if exists)
    
    For example:
    *   **Arugula Salad with Lemon Vinaigrette** A simple salad featuring fresh arugula.
        * Arugula
    
    You will return a recipe for the meal named and described. 
    The recipe must use each INGREDIENT.
    The recipe may use any other food ingredients.
    
    The recipe returned should adhere to this format:
    1. The name of the meal (MEAL_NAME) on the first line, followed by a blank line.
    2. The string 'Ingredients:' on its own line.
    3. A list of all ingredients, one per line, and including the cooking measurements for each ingredient
    4. The string 'Instructions:' on its own line.
    5. Step by step instructions for following the recipe, with each step delimited by a sequential numbered bullet.
    """,
    tools=[google_search],
)
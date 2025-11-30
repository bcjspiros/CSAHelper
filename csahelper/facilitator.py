from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from google.adk.models.google_llm import Gemini

from .agentconfig import retry_config
from .cookbook import cookbook

def output_recipe(recipe: str):
    """Receive recipe output from Cookbook and save the recipe as a text file in the agent_generated_recipes folder
    Args:
          recipe (str): The returned text from a call to the Cookbook.
    """
    # Need to clean up the recipe name to get a valid filename
    recipe_name = recipe.split('\n')[0].strip().lower()
    recipe_name = recipe_name.replace("*","").replace(" ","_")

    print(f'\n{recipe_name}\n')
    with open(f'agent_generated_recipes/{recipe_name}_recipe.md', 'w') as recipe_file:
        recipe_file.write(recipe)

facilitator = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="Facilitator",
    instruction="""Retrieve the series of meal suggestions from {mealplan}.
    Each entry in the series will have this format:
        *   **MEAL_NAME** DESCRIPTION
            * INGREDIENT
            * INGREDIENT (if exists)
    
    For example:
    *   **Arugula Salad with Lemon Vinaigrette** A simple salad featuring fresh arugula.
        * Arugula
    
    For each entry in the series perform the following steps in order:
        1. First, use the `Cookbook` agent to find a recipe for each entry in the series of meal suggestions.
        2. Next, after receiving a recipe from the Cookbook, use the `output_recipe()` method to output the text to the user.
    """,
    tools=[output_recipe, AgentTool(agent=cookbook)],
)

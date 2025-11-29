from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from google.adk.models.google_llm import Gemini

from .agentconfig import retry_config
from .cookbook import cookbook

def output_recipe(recipe: str):
    """Receive recipe output from Cookbook and outputs recipe to the user.
    Args:
          recipe (str): The returned text from a call to the Cookbook.
    """
    print(f'\n{recipe}\n')

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
    
    For each entry in the series perform the following steps:
        1. Use the `Cookbook` agent to find a recipe for each entry in the series of meal suggestions.
        2. Use the `output_recipe()` method to output the text returned by the Cookbook to the user.
    """,
    tools=[output_recipe, AgentTool(agent=cookbook)],
)

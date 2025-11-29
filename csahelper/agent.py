from google.adk.agents import Agent, SequentialAgent

from google.adk.models.google_llm import Gemini

from .agentconfig import retry_config
from .mealplanner import meal_planner
from .facilitator import facilitator

# Root agent
#root_agent = LlmAgent(
#    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
#    name="csahelper",
#    description="Agent to meal plan based on weekly CSA box contents",
#    instruction="""You are a meal planning agent.
#    You will be provided with a list of ingredients and will choose meals using these ingredients.
#    You must not provide a recipe for the meal, only a basic description of the meal.
#    Each ingredient must only appear in one meal.
#
#    For example, if given the ingredients bok choy, scallions, potatoes, and red onions:
#    You could suggest a stir-fry using the bok choy and scallions.
#    And you could suggest home fries with red onions for the potatoes and red onions.
#
#    You must return the meal description and the ingredients from the list used in that meal.""",
#    tools=[google_search],
#)

root_agent = SequentialAgent(
    name="CSAHelper",
    sub_agents=[meal_planner, facilitator],
)
# CSA Helper

Do you love your Community Supported Agriculture (CSA) share? Sure, we all do.   
But how many times have you opened your weekly box only to ask yourself "What the heck do I do with that?"

If so then CSA Helper is here to tell you "what to do with that?"

CSA helper takes a list of ingredients you don't know what to do with and plans some meals using those ingredients. It will write you out easy to follow recipes for each one, all without having to wade through someone's life story just to get to the list of ingredients.

## How to run

- Copy the `env-templete` to a `.env` file in the `csahelper` dir.
- Add your `GOOGLE_API_KEY` to the `.env` file
- Run from the `adk` command line with `adk run csahelper`. Type `exit` to exit.
- You can also use `adk web` 

## Getting some recipes

Simply ask the agent for recipes using a list of desired ingredients.

> Please plan meals based on these ingredients: kohlrabi, red turnips, leeks, celery, and potatoes

Each recipe will be written in Markdown to the `agent_generated_recipes` folder.

## Cautions

This is a very early prototype and can be a little brittle right now, so please be nice to the Helper and don't feed it anything non-edible.

## Future features?

- Saving user preferences, including dietary restrictions and allergies.
- Writing out a shopping list for all ingredients needed for the recipes it outputs.
- Planning a full week of meals, filling in basic filler meals like pasta or eating out for days when you don't want to cook from your CSA box.
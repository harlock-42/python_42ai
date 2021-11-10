class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		try:
			# check if the arguments has the right type
			if type(name) != str or type(cooking_lvl) != int or type(cooking_time) != int or type(ingredients) != list or type(description) != str or type(recipe_type) != str:
				raise ValueError("wrong value type")
			# check the containt of the values
			if cooking_lvl < 1 or cooking_lvl > 5:
				raise ValueError("cooking_lvl has to be in a range between 1 and 5")
			if cooking_time < 0:
				raise ValueError("cooking time has to be a positive number")
			if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
				raise ValueError("recipe_type can be \"starter\", \"lunch\" or \"dessert\"")
			if name == "" or ingredients == []:
				raise ValueError("empty value")
		except ValueError as ve:
			print(ve)

		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		nb_ingredients = len(self.ingredients)
		return f'\n{self.name} is a {self.recipe_type} wich takes {nb_ingredients} ingredients as follow:\n\n\
{self.ingredients}\n\n\
It takes {self.cooking_time} minutes with a difficultie of {self.cooking_lvl} on 5\n\n\
Description :\n\
{self.description}'
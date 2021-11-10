from recipe import Recipe
from datetime import datetime

class Book:
	def __init__(self, name, recipe_list):
		try:
			if type(name) != str or type(recipe_list) != dict:
				raise TypeError("wrong type attributes")
		except TypeError as tp:
			print(tp)
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
		self.recipe_list = recipe_list
		pass
	def get_recipe_by_name(self, name):
		try:
			if type(name) != str:
				raise TypeError("wrong type name")
		except TypeError as tp:
			print(tp)
		for key, value in self.recipe_list.items():
			for elem in self.recipe_list[key]:
				if name == elem.name:
					print(elem)
					return (elem)
		return None
	def get_recipes_by_types(self, recipe_type):
		try:
			if type(recipe_type) != str:
				raise TypeError("wrong type attribute")
		except TypeError as tp:
			print (tp)
		liste = []
		for key in self.recipe_list:
			if key == recipe_type:
				for elem in self.recipe_list[key]:
					liste.append(elem.name)
		if liste != []:
			print(liste)
			return liste
		return None
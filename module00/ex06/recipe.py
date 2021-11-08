from termcolor import *
import colorama

def print_only_keys():
	print()
	print ("Recipes are : ", end="")
	for key, values in cookbook.items():
		print (key + " ", end="")
	print()
	print()

def print_only_values(cookbook):
	for key, values in cookbook.items():
		for key_nested in values:
			if key_nested == 'ingredients':
				for i in values[key_nested]:
					cprint (i, "yellow")
			else:
				cprint(values[key_nested], "green")

def print_recipe(recipe):
	print ("The recipe is : ", end="")
	for i in cookbook[recipe]['ingredients']:
		print (i + " ", end="")
	print ("")
	print ("this ", end="")
	print (cookbook[recipe]['meal'], end="")
	print (" takes ", end="")
	print (cookbook[recipe]['prep_time'])

def print_all_items(cookbook):
	for key, values in cookbook.items():
		cprint (key, "red")
		print ()
		for key_nested in values:
			cprint (key_nested, "white")
			print ()
			if key_nested == 'ingredients':
				for i in values[key_nested]:
					cprint (i, "green")
				print ()
			else:
				cprint(values[key_nested], "green")
				print ()

	cookbook[str(recipe)]

def del_recipe(recipe):
	del cookbook[recipe]

def add_recipe(recipe_name, ingredient, meal, prep_time):
	cookbook[recipe_name] = {'ingredients': ingredient, 'meal': meal, 'prep_time': prep_time}

def print_all_recipe_name():
	for key, values in cookbook.items():
		print (key)

def print_prompt():
	print ("Please select an option by typing the corresponding number:")
	print ("1: Add recipe")
	print ("2: Delete a recipe")
	print ("3: Print a recipe")
	print ("4: Print the cookbook")
	print ("5: Quit")
	return input (">> ")

def is_recipe_exist(recipe):
	for key, values in cookbook.items():
		if key == recipe:
			return True
	return False

def do_order(nb):
	if nb == 1:
		print ()
		print ("Please write the name of your recipe : ", end="")
		recipe_name = input("")
		print ("Please write the ingredients needed : ", end="")
		ingredients = input("")
		print ("Please write the kind of meal : ", end="")
		meal_kind = input("")
		ingredients_list = list(ingredients)
		print ("Please write the time of preparation : ", end="")
		preparation_time = input("")
		add_recipe(recipe_name, ingredients.split(), meal_kind, preparation_time)
	elif nb == 2:
		print ("\nPlease enter the recipe's name you want to remove :")
		arg = input(">> ")
		if is_recipe_exist(arg) == True:
			del_recipe(arg)
		else:
			print("Recipe does not exist")
	elif nb == 3:
		print ("\nPlease enter the recipe's name to get its details :")
		arg = input(">> ")
		if is_recipe_exist(arg) == True:
			print_recipe(arg)
		else:
			print("Recipe does not exist")
	elif nb == 4:
		print_only_keys()
	cprint("Please press enter to continue..", "grey")
	input()



colorama.init()

cookbook = {}
cookbook['sandwich'] = {'ingredients': ["ham", "bread", "cheese", "tomatoes"], 'meal': 'lunch', 'prep_time': '10 minutes of preparation'}
cookbook['cake'] = {'ingredients': ["flour", "sugar", "eggs"], 'meal': 'desert', 'prep_time': '60 minutes of preparations'}
cookbook['Salad'] = {'ingredients': ["avocado", "arugula", "tomatoes", "spinach"], 'meal': 'lunch', 'prep_time': '15 minutes of preparation'}

#print_only_keys(cookbook)
#print_only_values(cookbook)
#print_all_items(cookbook)
#print_recipe('sandwich')
#del_recipe('cake')
#add_recipe("yasa", ["ognon", "mustards", "soja"], 'lunch', '20 minutes of preparation')
#print_all_recipe_name()

nb = 0

while nb != 5:
	stdin = print_prompt()
	if stdin.isdecimal() == True:
		nb = int(stdin)
	do_order(nb)
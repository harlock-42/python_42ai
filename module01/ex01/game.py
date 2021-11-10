class GotCharacter:
	def __init__(self, first_name, is_alive=True):
		try:
			if type(first_name) != str:
				raise TypeError("First name must be str type")
			if first_name == "":
				raise ValueError("First name missing")
			if is_alive != True or is_alive != False:
				raise ValueError("is_alive must be a bool")
		except TypeError as tp:
			print("Ty2peError: " + tp)
		except ValueError as ve:
			print("ValueError: " + ve)

class Stark(GotCharacter):
	def __init__(self, first_name, is_alive=True)
		super().__init__(self, first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

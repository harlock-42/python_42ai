def deco(func):
	def inner():
		print("Maison.. Telephone.. Maison..")
		return func()
	return inner

@deco # deco(gertie)
def gertie():
	print("Je lui ai appris a parler ! Ecoute !")

@deco # deco(elliott)
def elliott():
	print("Il veut rentrer chez lui !")

gertie()
elliott()
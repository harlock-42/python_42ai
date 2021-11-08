import sys

def isOnlyNumber(value):
	try:
		if value[0] == '-':
			value = value[1:]
		if not value.isdigit():
			return False
		return True
	except ValueError:
		return False

if len(sys.argv) > 3:
	print("InputError: too many arguments")
elif len(sys.argv) < 3:
	print("InputError: too few arguments")
elif not isOnlyNumber(sys.argv[1]) or not isOnlyNumber(sys.argv[2]):
	print("InputError: only numbers")
else:
	nb1 = int(sys.argv[1])
	nb2 = int(sys.argv[2])
	print("Sum:		" + str(nb1 + nb2))
	print("Difference:	" + str(nb1 - nb2))
	print("Product		" + str(nb1 * nb2))
	if nb2 == 0:
		print("Quotient:	ERROR (div by zero)")
		print("Remaider:	ERROR (div by zero)")
	else:
		print("Quotient:	" + str(nb1 / nb2))
		print("Remaider:	" + str(nb1 % nb2))

import sys

if len(sys.argv) == 2:
	if sys.argv[1].isdecimal() == True:
		nb = int(sys.argv[1])
		if nb == 0:
			print("I'm Zero")
		elif nb % 2 == 0:
			print("I'm Even")
		else:
			print("I'm Odd")
	else:
		print("ERROR")
else:
	print("ERROR")
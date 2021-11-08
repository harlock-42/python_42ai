from termcolor import *
import colorama
import sys
import string

len_arg = len(sys.argv)
if len_arg != 3:
	cprint("ERROR", "red")
	sys.exit()
if sys.argv[2].isdecimal() == False:
	cprint("ERROR", "red")
	sys.exit()
n = int(sys.argv[2])
punct = string.punctuation
liste = sys.argv[1].split()
liste = [x for x in liste if len(x) > n]
i = 0
while i < len (liste):
	liste[i] = "".join([char for char in liste[i] if char not in punct])
	i += 1
print (liste)
import sys
from termcolor import *
import colorama

def check_input(liste, end):
	i = 1
	while i < end:
		liste[i] = liste[i].lower()
		for c in liste[i]:
			if c not in morse:
				print (c)
				return False
		i += 1
	return True

morse = {
'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

len_arg = len(sys.argv)
if len_arg < 2:
	cprint ("ERROR", "red")
	sys.exit()
liste = sys.argv
if check_input(liste, len_arg) == False:
	cprint ("ERROR", "red")
	sys.exit()
i = 1
while i < len_arg:
	for c in liste[i]:
		print (morse[c], end="")
	i += i
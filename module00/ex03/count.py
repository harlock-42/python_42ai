import string

def text_analyzer(arg):
	print("- " + str(sum(map(str.isupper, arg))) + " upper letters")
	print("- " + str(sum(map(str.islower, arg))) + " lower letters")
	count = 0
	for c in arg:
		if c in string.punctuation:
			count += 1
	print("- " + str(count) + " punctuations marks")
	print("- " + str(arg.count(' ')) + " spaces")
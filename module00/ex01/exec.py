import sys

n = len(sys.argv)
i = 1
if (n != 1):	
	string = sys.argv[i]
	while (i < n - 1):
		string = string + " " + sys.argv[i + 1]
		i = i + 1
	string = string[::-1]
	print(string)
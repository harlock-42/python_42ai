t = (2, -4, 100)

print("The " + str(len(t)) + " numbers are: " + str(t[1]), end="")
t = t[1:]
for nb in t:
	print(", " + str(nb), end="")
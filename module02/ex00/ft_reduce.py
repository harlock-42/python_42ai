import operator
def ft_reduce(func, iterable):
	try:
		if isinstance(iterable, (dict, list, tuple, set)) == False:
			raise TypeError("Second parameter of map function must be an iterable")
	except TypeError as tp:
		print("TypeError: ", end="")
		print(tp)
	else:
		res = 0
		for elem in iterable:
			res = func(res, elem)
		return res
print(ft_reduce(operator.add, [1, 2, 3]))
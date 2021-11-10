def ft_filter(func, iterable):
	try:
		if isinstance(iterable, (dict, list, tuple, set)) == False:
			raise TypeError("Second parameter of map function must be an iterable")
	except TypeError as tp:
		print("TypeError: ", end="")
		print(tp)
	else:
		for elem in iterable:
			if func(elem) == True:
				yield elem
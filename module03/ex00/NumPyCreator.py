import numpy

class npc:
	def __init__(self):
		pass
	def from_list(lst):
		try:
			if type(lst) != list:
				raise TypeError("The argument must be a list")
		except TypeError as te:
			print("TypeError: ", tp)
		return numpy.array(lst)
	def from_tuple(tpl):
		try:
			if type(tpl) != tuple:
				raise TypeError("The argument must be a tuple")
		except TypeError as te:
			print("TypeError: ", tp)
		return numpy.asarray(tpl)
	def from_iter(iterable):
		try:
			if isinstance(iterable, (list, tuple, dict)) == False:
				raise TypeError("Argument must be an iterable")
		except TypeError as te:
			print("TypeError: ", tp)
		return numpy.fromiter(iterable, int)
	def from_shape(shape, value=0):
		try:
			if isinstance(shape, tuple) == False or len(shape) != 2:
				raise TypeError("Argument must be a range")
		except TypeError as te:
			print("TypeError: ", tp)
		return numpy.full(shape, value)
	def random(shape):
		try:
			if isinstance(shape, tuple) == False or len(shape) != 2:
				raise TypeError("Argument must be a range")
		except TypeError as te:
			print("TypeError: ", tp)
		return numpy.empty(shape)


# arr = npc.from_list([[1, 2, 3, 4], [0, 2, 4, 6]])
arr = npc.random((2, 2))
print(arr)
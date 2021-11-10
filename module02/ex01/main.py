def	what_are_the_vars(*args, **kwargs):
	obj = ObjectC()
	for num, var in enumerate(args):
		setattr(obj, "var_" + str(num), var)
	for key, value in kwargs.items():
		if getattr(obj, key, None) != None:
			return None
		setattr(obj, key, value)
	return obj
	# setattr(obj, args[0], 3)
	# for var in args:
		# getattr()
	pass
class ObjectC(object):
	def __init__(self):
		pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

obj = what_are_the_vars(12, var_=2)
doom_printer(obj)
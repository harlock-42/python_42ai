class File(object):
	def __init__(self, file_name= None, sep=",", header=False, skip_top=0, skip_bottom=0):
		self.file_obj = open(file_name, "r")
	def __enter__(self):
		return self.file_obj
	def __exit__(self, type, value, traceback):
		self.file_obj.close()

with File("good.csv") as f:
	line = f.readline()
	while line:
		print(line, end="")
		line = f.readline()
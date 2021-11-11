class File(object):
	def __init__(self, file_name= None, sep=",", header=False, skip_top=0, skip_bottom=0):
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file_obj = open(file_name, "r")
	def __enter__(self):
		return self.file_obj
	def __exit__(self, type, value, traceback):
		self.file_obj.close()
	def getdata(self):
		data = self.file_obj.readline()
		data = data.split(",")
		res = []
		header = []
		if self.header == False:
			res.append(data)
		else:
			header.append(data)
		while data:
			data = self.file_obj.readline()
			data1 = data.split(self.sep)
			if data:
				res.append(data1)
		res = res[self.skip_top:]
		if self.skip_bottom > 0:
			index = self.skip_bottom * -1
			res = res[:index]
		return res
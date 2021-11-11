from PIL import Image
from matplotlib import pyplot as plt
import numpy

class ImageProcessor:
	def __init__(self):
		pass
	def load(self, path):
		img = Image.open("harlock.png")
		arr = numpy.array(img)
		print("Loading an image of dimensions " + str(arr.shape[0]) + " x " + str(arr.shape[1]))
		return arr
	def display(self, array):
		plt.imshow(array)
		plt.show()

ip = ImageProcessor()
img = ip.load("harlock.png")
ip.display(img)
# print(img)
import numpy as np
import random
from csvreader import File

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids
	def fit(self, X):
		self.centroids = np.zeros((self.ncentroid, 3))
		# generate random centroids
		for arr in self.centroids:
			arr[0] = random.uniform(float(min(X[:, 1])), float(max(X[:, 1])))
			arr[1] = random.uniform(float(min(X[:, 2])), float(max(X[:, 2])))
			arr[2] = random.uniform(float(min(X[:, 3])), float(max(X[:, 3])))
		cluster = [[] for i in range(self.ncentroid)] # init cluster where we are going to place the civilians
		# compute the distance between each point of each centroid
		for point in X:
			dist = []
			for index, centroid in enumerate(self.centroids):
				vec_centroid = np.array((float(centroid[0]), float(centroid[1]), float(centroid[2])))
				vec_point = np.array((float(point[1]), float(point[2]), float(point[3])))
				dist.append(np.linalg.norm(vec_point - vec_centroid))
			cluster[dist.index(min(dist))].append([float(point[0]), float(point[1]), float(point[2]), float(point[3])])
		# comput the average coordinate centroid

		for centroid in cluster:
		
		# 	for elem in center:
		# 		print(elem)
		a = np.array((1, 1, 1))
		b = np.array((1, 1, 1))
		print(np.linalg.norm(a-b))
		pass

file = File("solar_system_census.csv", header=True, sep=",")
data = file.getdata()
arr = np.array(data)
KC = KmeansClustering(1, 4)
KC.fit(arr)

# KC = KmeansClustering(1, 4)
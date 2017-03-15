import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('seaborn-dark')

X = np.array([[1,2], [1.5,1.8], [5,8], [8,8], [1,0.6], [12,15], [1,3],[8,9],[0,3], [5,4], [8,4], [11,14], [13,18],[15,17]])

class Mean_Shift:
	def __init__(self, radius=5):
		self.radius = radius

	def fit(self,data):
		centroids = {}

		for i in range(len(data)):
			centroids[i] = data[i] # each featureset is its own cluster center to start

		while True:
			new_centroids = []
			for i in centroids:
				in_bandwidth = [] #all featuresets within the bandwidth
				centroid = centroids[i]
				for featureset in data:
					if np.linalg.norm(featureset - centroid) < self.radius:
						in_bandwidth.append(featureset)

				new_centroid = np.average(in_bandwidth, axis = 0)
				new_centroids.append(tuple(new_centroid))

			uniques = sorted(list(set(new_centroids))) # set is unique elements in a list

			prev_centroids = dict(centroids)

			centroids = {}
			for i in range(len(uniques)):
				centroids[i]= np.array(uniques[i])

			optimized = True

			for i in centroids:
				if not np.array_equal(centroids[i], prev_centroids[i]):
					optimized = False

				if not optimized:
					break

			if optimized:
				break

		self.centroids = centroids

	def predict(self,data):
		pass


clf = Mean_Shift()
clf.fit(X)

centroids = clf.centroids

plt.scatter(X[:,0], X[:,1])

for c in centroids:
	plt.scatter(centroids[c][0], centroids[c][1], color = 'k', marker = '*')
plt.show()


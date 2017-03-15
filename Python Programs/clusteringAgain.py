import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('seaborn-dark')

X = np.array([[1,2], [1.5,1.8], [5,8], [8,8], [1,0.6], [12,15], [1,3],[8,9],[0,3], [5,4], [8,4]])
colors = 10*["g", "r" , "c", "b", "k", "m"]

# when accessing a dictionary, calling the key returns the values associated with that key
class K_Means:
	def __init__(self, k = 2, tol = 0.001, max_iter = 300):
		self.k = k
		self.tol = tol
		self.max_iter = max_iter


	# training the classifier (clusterer)
	def fit(self, data):
		self.centroids = {}  # empty dictionary for now

		for i in range(self.k): # how many clusters do we want the machine to create
			self.centroids[i] = data[i] # arbitrarily picking centroids as first kth elements of data
		for i in range(self.max_iter):
			self.classifications = {}   # empty dictionary for classifiying data points

			for i in range(self.k):   # iterating through number of clusters
				self.classifications[i] = [] # classifying data points into k clusters

			# classify each featureset into one of the clusters based on distance from centroid
			for featureset in data: # each list within the list of data
				# want to find Euclidean distance between each set of coordinates and k centroids
				distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
				classification = distances.index(min(distances))
				self.classifications[classification].append(featureset) # keys in classifications dictionary are k clusters and values are the featuresets in each cluster (closest to the centroid)

			prev_centroids = dict(self.centroids)

			# now create new centroids based on the average location of featuresets within a cluster
			for classification in self.classifications:
				self.centroids[classification] = np.average(self.classifications[classification], axis = 0)

			optimized  = True

			# now need to figure out if tolerance has been met
			for c in self.centroids:
				original_centroid = prev_centroids[c]
				current_centroid = self.centroids[c]
				#figuring out the percentage change between the previous centroid and the new centroid
				if np.sum((current_centroid - original_centroid)/original_centroid*100) > self.tol:
					print(np.sum((current_centroid - original_centroid)/original_centroid*100))
					optimized = False # if the percentage change is larger than the tolerance, the classfication into k clusters is not complete

			if optimized:
				break


	def predict(self,data):
		distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
		classification = distances.index(min(distances))
		return classification


clf = K_Means()
clf.fit(X)

# plotting the centroids
for centroid in clf.centroids:
	plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], marker = 'o', color = 'k')

for classification in clf.classifications:
	color = colors[classification]
	for featureset in clf.classifications[classification]:
		plt.scatter(featureset[0], featureset[1], marker = 'x', color = color)
'''	
unknowns = np.array([[1,3],[8,9],[0,3], [5,4], [8,4]])
for unknown in unknowns:
	classification = clf.predict(unknown)
	plt.scatter(unknown[0], unknown[1], marker = '*', color = colors[classification])
'''
plt.show()
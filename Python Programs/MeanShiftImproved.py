import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
from sklearn.datasets.samples_generator import make_blobs
import random
style.use('seaborn-dark')

centers = random.randrange(2,8)

X , y = make_blobs(n_samples = 50, centers = centers, n_features=2)

#X = np.array([[1,2], [1.5,1.8], [5,8], [8,8], [1,0.6], [12,15], [1,3],[8,9],[0,3], [5,4], [8,4], [11,14], [13,18],[15,17]])
colors = 10*["g", "r" , "c", "b", "k", "m"]

class Mean_Shift:
	def __init__(self, radius= None, radius_norm_step = 50): # need a way to choose the radius to "make sense" with the data, dynamically adjusted
		# want to wait points closer to the centroid more highly for calculating the new centroid
		self.radius = radius
		self.radius_norm_step = radius_norm_step
	def fit(self,data):

		# first finf the average location of all the featuresets
		if self.radius == None:
			all_data_centroid = np.average(data, axis = 0)
			all_data_norm = np.linalg.norm(all_data_centroid) # distance from origin (one argument to norm)
			self.radius = all_data_norm / self.radius_norm_step

		centroids = {}

		for i in range(len(data)):
			centroids[i] = data[i] # each featureset is its own cluster center to start

		
		weights = [ i for i in range(self.radius_norm_step)][::-1] # reverse the list
		while True:
			new_centroids = []
			for i in centroids:
				in_bandwidth = [] #all featuresets within the bandwidth
				centroid = centroids[i]
				#weights = [ i for i in range(self.radius_norm_step)][::-1] # reverse the list


				for featureset in data:
					distance = np.linalg.norm(featureset-centroid)
					if distance == 0:
						distance = 0.000000001
					weight_index = int(distance/self.radius) # how many radius steps taken away from the centroid
					# closer points are weighted more heavily
					if weight_index > self.radius_norm_step-1: # if point is outside of the radius norm step, set the weight to 0
						weight_index = self.radius_norm_step-1
					to_add = (weights[weight_index]**2)*[featureset]
					in_bandwidth += to_add




				new_centroid = np.average(in_bandwidth, axis = 0)
				new_centroids.append(tuple(new_centroid))

			uniques = sorted(list(set(new_centroids))) # set is unique elements in a list

			to_pop = []
			for i in uniques:
				for ii in [i for i in uniques]:
					if i == ii:  # centroid is itself
						pass 

					elif np.linalg.norm(np.array(i)-np.array(ii)) <= self.radius:
						to_pop.append(ii) # do not modify a list as you iterate through the list
						break

			for i in to_pop:
				try:
					uniques.remove(i)
				except:
					pass


			prev_centroids = dict(centroids)

			centroids = {}
			for i in range(len(uniques)):
				centroids[i]= np.array(uniques[i])
			

			optimized = True

			for i in centroids:
				if not np.array_equal(centroids[i], prev_centroids[i]):
					optimized = False

			if optimized:
				break

		self.centroids = centroids
		self.classifications = {}
		

		for i in range(len(self.centroids)):
			self.classifications[i] = []

		for featureset in data:
			# compare distance to centroids
			distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
			classification = (distances.index(min(distances)))
			self.classifications[classification].append(featureset) # featureset is a part of the cluster


	def predict(self,data):
		distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
		classification = distances.index(min(distances))
		return classification


clf = Mean_Shift()
clf.fit(X)

centroids = clf.centroids

print('Number of centers of \'blobs\' = %d' % centers)
print('Number of centroids = %d' %len(centroids))
print(centroids)

#plt.scatter(X[:,0], X[:,1])
for classification in clf.classifications:
	color = colors[classification]
	for featureset in clf.classifications[classification]:
		plt.scatter(featureset[0], featureset[1], marker = 'x', color = color)

for c in centroids:
	plt.scatter(centroids[c][0], centroids[c][1], color = 'k', marker = '*')
plt.show()


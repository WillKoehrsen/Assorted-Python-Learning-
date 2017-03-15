import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style
from sklearn import preprocessing 
import pandas as pd 
import time

start_time = time.time()

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
					#print(np.sum((current_centroid - original_centroid)/original_centroid*100))
					optimized = False # if the percentage change is larger than the tolerance, the classfication into k clusters is not complete

			if optimized:
				break


	def predict(self,data):
		distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
		classification = distances.index(min(distances))
		return classification

df = pd.read_excel('titanic.xls')
df.drop(['body', 'name', 'ticket'], 1, inplace = True)
df.fillna(0, inplace = True)

def handle_non_numerical_data(df):

	columns = df.columns.values

	for column in columns:
		text_digit_vals = {}
		def convert_to_int(val):
			return text_digit_vals[val]

		# if the data is not numeric, need a way to convert to consistent number for each string
		if df[column].dtype != np.int64 and df[column].dtype != np.float64:
			column_contents = df[column].values.tolist()
			unique_elements = set(column_contents)
			x = 0

			for unique in unique_elements:
				if unique not in text_digit_vals:
					#creating a dictionary with new id per unique string
					text_digit_vals[unique] = x
					x += 1

			df[column] = list(map(convert_to_int, df[column]))

	return df

df = handle_non_numerical_data(df)

X = np.array(df.drop(['survived'],1).astype(float))
y = np.array(df['survived'])

clf = K_Means()
clf.fit(X)

correct = 0
for i in range(len(X)):
	predict_me = np.array(X[i].astype(float))
	predict_me = predict_me.reshape(-1, len(predict_me))
	prediction = clf.predict(predict_me)
	if prediction == y[i]:
		correct += 1

print('Accuracy %0.3f' % ((correct/len(X)*100)))

print('Time elapsed = %0.3f seconds.' % (time.time()- start_time))

from math import sqrt
import numpy as np 
import warnings
import matplotlib.pyplot as plt 
from matplotlib import style
from collections import Counter
import random
import pandas as pd 
from classifierTut import classifier 


def k_nearest_neighbors(data, predict, k):
	if len(data) >= k:
		warnings.warn('K is set to a value less than or equal to the total number of voting groups (labels in dictionary)')
	distances = []
	for group in data:
		for features in data[group]:
			# euclidean_distance = sqrt(sum( [ features - predict**2 for i in range(len(features)) ] ))
			#euclidean_distance = np.sqrt(np.sum((np.array(features)- np.array(predict))**2))
			euclidean_distance = np.linalg.norm(np.array(features)- np.array(predict))
			distances.append([euclidean_distance, group])

	#print(sorted(distances)[0:k])
	votes = [i[1] for i in sorted(distances)[:k]]
	vote_result = Counter(votes).most_common(1)[0][0] # Counter.most_common returns a tuple within a list with [(most common, instances)]
	confidence = (Counter(votes).most_common(1)[0][1] / k )
	
	return vote_result, confidence

accuracies = []
confidences = []
test_number = 25 
for i in range(test_number):

	df = pd.read_csv("breast-cancer-wisconsin.data.txt")
	df.replace('?', -99999, inplace = True)
	df.drop(['id'], 1,  inplace = True) # drop id column because it is not a relevant feature
	full_data = df.astype(float).values.tolist() # make sure all values are floats, some might not be initially

	random.shuffle(full_data)
	test_size = 0.2
	train_set = {2:[], 4:[]}
	test_set = {2:[], 4:[]}
	train_data = full_data[:-int(test_size*len(full_data))] # training set is first 1-test_size of data
	test_data = full_data[-int(test_size*len(full_data)):] # test set is last test_size of data

	for i in train_data:
		train_set[i[-1]].append(i[:-1])

	for i in test_data:
		test_set[i[-1]].append(i[:-1])

	correct = 0
	total = 0
	confidence = []
	for group in test_set:
		for data in test_set[group]:
			vote, single_confidence = k_nearest_neighbors(train_set, data, k = 5)
			confidence.append(single_confidence)
			if group == vote:
				correct += 1
			total += 1

	#print('Accuracy: %0.4f' % ((correct/total) * 100))
	#print('Average confidence: %0.4f' % (np.mean(confidence)*100))
	accuracies.append(correct/total)
	confidences.append(confidence)

built_in_accuracy = classifier(25)
print('Average accuracy across %d' %test_number , 'tests = % 0.4f' % np.mean(accuracies))
print('Average confidence across %d' %test_number , 'tests = % 0.4f' % np.mean(confidences))
print('Average accuracy from built-in KNearestNeighbors across %d' %test_number , 'tests = % 0.4f' % np.mean(built_in_accuracy))
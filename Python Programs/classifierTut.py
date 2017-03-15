import numpy as np 
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd 

def classifier(test_number):
	accuracies = []
	for i in range(test_number):
		df = pd.read_csv('breast-cancer-wisconsin.data.txt')
		df.replace('?', -99999, inplace= True) # modify data frame

		# id, clump_thickness, unif_cell_size, unif_cell_size, marg_adhesion, single_epith_cell_size, bare_nuclei, bland_chrom, norm_nucleoli, mitoses, class
		# drop useless data: id is irrelevant to the data, is not a feature
		df.drop(['id'], 1, inplace = True)

		X = np.array(df.drop(['class'],1))
		y = np.array(df['class'])

		X_train, X_test, y_train, y_test = train_test_split(X , y, test_size = 0.2)

		clf=neighbors.KNeighborsClassifier(n_jobs = 32)
		clf.fit(X_train, y_train)
		accuracy = (clf.score(X_test, y_test)) # accuracy is different from confidence, the answers to the test are known
		#print(accuracy)
		'''
		example_measures = np.array([[4,2,1,1,1,2,3,2,1]]) 
		example_measures2 = np.array([[3,2,1,2,3,5,3,3,1]]) # use to predict
		example_measures = example_measures.reshape(len(example_measures),-1) # need to reshape for classifier
		example_measures2 = example_measures2.reshape(len(example_measures2),-1)
		prediction = clf.predict(example_measures)
		prediction2 = clf.predict(example_measures2)
		print(prediction, prediction2)
		'''
		accuracies.append(accuracy)
	return(accuracies)


test_number = 25
accuracies = classifier(test_number)

if __name__ == "__main__":
	print('Average accuracy across %d' %test_number , 'tests = %0.4f' % np.mean(accuracies))
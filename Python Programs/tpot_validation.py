import numpy as np 
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import FunctionTransformer


digits = load_digits()

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, 
													train_size = 0.75, test_size = 0.25)

number_of_tests = 10
accuracy1 = []
accuracy2 = []

for i in range(number_of_tests):

	clf1 = KNeighborsClassifier(n_neighbors = 5, weights = 'distance')
	clf1.fit(X_train, y_train)

	accuracy1.append(clf1.score(X_test, y_test))

	clf2 = VotingClassifier([('est', LogisticRegression(C= 30.0, dual = False, penalty = 'l2'))])
	clf2.fit(X_train, y_train)

	accuracy2.append(clf2.score(X_test, y_test))

print('Accuracy from clf1 = %0.3f ' % (np.mean(accuracy1)*100))
print('Accuracy from clf1 w/out preprocessing = %0.3f ' % (np.mean(accuracy2)*100))
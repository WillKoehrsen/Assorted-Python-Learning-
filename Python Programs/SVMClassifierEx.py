import numpy as np 
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd 
from sklearn import svm


df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?', -99999, inplace= True) # modify data frame

# id, clump_thickness, unif_cell_size, unif_cell_size, marg_adhesion, single_epith_cell_size, bare_nuclei, bland_chrom, norm_nucleoli, mitoses, class
# drop useless data: id is irrelevant to the data, is not a feature
df.drop(['id'], 1, inplace = True) # if ID column is not dropped, the accuracy falls precipitously

X = np.array(df.drop(['class'],1)) # features
y = np.array(df['class']) # labels

X_train, X_test, y_train, y_test = train_test_split(X , y, test_size = 0.2)

# support vector machine. support vector classifier
clf=svm.SVC()
clf.fit(X_train, y_train)
accuracy = (clf.score(X_test, y_test)) 
print('Accuracy = %0.3f' % accuracy)
import numpy as np 
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd 



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
print('Accuracy = %0.3f' % accuracy)
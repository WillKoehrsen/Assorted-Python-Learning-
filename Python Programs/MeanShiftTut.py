import matplotlib.pyplot as plt 
from matplotlib import style 
import numpy as np 
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
import pandas as pd 
import time
from sklearn.cluster import MeanShift

start_time = time.time()
style.use('seaborn-dark')

'''
Pclass Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
survival Survival (0  No; 1 = Yes)
name Name
sex Sex
age Age
sibsp Number of Siblings/Spouses Aboard
parch Number of Parents/Children Aboard
ticket Ticket Number
fare Passenger Fare (British pound)
cabin Cabin
embarked Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
boat Lifeboat
body Body Identification Number
home.dest Home/Destination
'''

# label = survived ; features = ?? (not ticket number probably)
# female = 0 ; male = 1
df = pd.read_excel('titanic.xls')
original_df = pd.DataFrame.copy(df)

df.drop(['body', 'name', 'boat', 'ticket'], 1, inplace = True)
#df.convert_objects(convert_numeric=True)
df.fillna(0, inplace = True)


def handle_non_numerical_data(df):
	columns = df.columns
	for column in columns:
		text_digit_vals = {}
		def convert_to_int(val):
			return text_digit_vals[val]

		if df[column].dtype != np.int64 and df[column].dtype != np.float64:
			column_contents = df[column].values.tolist()
			unique_elements = set(column_contents)
			x = 0
			for unique in unique_elements:
				if unique not in text_digit_vals:
					text_digit_vals[unique] = x
					x += 1

			df[column] = list(map(convert_to_int, df[column]))

	return df


df = handle_non_numerical_data(df)
X = np.array(df.drop(['survived'],1).astype(float))
X = preprocessing.scale(X) # normalize each column
y = np.array(df['survived'])

clf = MeanShift()
clf.fit(X)

labels = clf.labels_
cluster_centers = clf.cluster_centers_

original_df['cluster_group']= np.nan

for i in range(len(X)):
	original_df['cluster_group'].iloc[i] = labels[i] #go throught the first row and put in the label that MeanShift identified

n_clusters_ = len(np.unique(labels)) # the number of clusters is equal to the number of unique labels decided by MeanShift

survival_rates = {}

for i in range(n_clusters_):
	temp_df = original_df[ (original_df['cluster_group'] == float(i)) ]
	survival_cluster = temp_df[ (temp_df['survived'] ==1) ]
	survival_rate = len(survival_cluster) /len(temp_df)
	survival_rates[i] = survival_rate

print(survival_rates)
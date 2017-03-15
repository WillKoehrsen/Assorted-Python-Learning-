from statistics import mean
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats.stats import pearsonr
from matplotlib import style
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import random

style.use('seaborn')

#xs = np.array([1,2,3,4,5, 6], dtype = np.float64)
#ys = np.array([5,4,6,5,6, 7], dtype = np.float64)

def create_dataset(hm, variance, step=2, correlation=False):
	val = 1
	ys= []
	for i in range(hm):
		y = val + random.randrange(-variance, variance)
		ys.append(y)
		if correlation and correlation == 'pos':
			val += step
		elif correlation and correlation =='neg':
			val -= step
	xs = [i for i in range(len(ys))]
	return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def best_fit_parameters(xs, ys):
	m = ( ( (mean(xs) * mean(ys)) - mean(xs*ys) ) /
		( (mean(xs)**2) - mean(xs**2)) )
	b = mean(ys) - (m * mean(xs))
	return m, b

xs , ys =create_dataset(40, 10, 2, correlation ='pos')
m , b = best_fit_parameters(xs, ys)
regression_line = [(m*x) + b for x in xs]

index = 0
y_hat_error = 0
y_bar_error = 0
for prediction in regression_line:
	y_hat_error += (abs(ys[index]-prediction))**2
	y_bar_error += (abs(ys[index]-mean(ys)))**2
	index += 1

r_squared = 1 - y_hat_error/y_bar_error

print(r_squared)

'''
x_stdev = np.std(xs) # sample standard deviation of x
y_stdev = np.std(ys)  # sample standard deviation of y
# pearsonr = sample correlation coefficient
m_alt = (pearsonr(xs, ys)[0]) * (y_stdev/x_stdev) 
'''

X = xs.reshape(-1,1)  # features
y = ys.reshape(-1, 1) # labels

# split the sample into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size = 0.2, random_state = 0)
clf = LinearRegression() # assign the algorithm for the classifier
clf.fit(X_train, y_train) # train the classifier
data_predict = np.array([[45],[56],[34],[56]])

#print(clf.predict(data_predict))
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.title('R-squared = %0.4f' % r_squared)
plt.show()
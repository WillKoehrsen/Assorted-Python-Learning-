import pandas as pd 
import quandl, math, datetime, pickle
import numpy as np 
from sklearn import preprocessing,svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('seaborn-dark')

df = quandl.get('WIKI/GOOGL')
print(df.tail())

df = df[['Adj. Open','Adj. High' , 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# features to use for classification

# percentage difference between the day's high price and the closing price, how far off the high did the stock close
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
#percentage change between the day's opening price and the day's closing price, did the stock move up or down
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change','Adj. Volume']] # only keep the important features

forecast_col = 'Adj. Close'
# replace any nan (not a number) with some data, outlier in data
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01 * len(df))) # try to predict out 10% of the days in the dataframe, use data for 10% of days ago to predict today

# the price was this so many days ago, so based on that, predict it will be this
df['label'] = df[forecast_col].shift(-forecast_out) # feature is adjusted close from 10 percent of days in the future

X = np.array(df.drop(['label'],1)) # features
X = preprocessing.scale(X)
X_lately = X[-forecast_out:] # X_lately is the last ten percent of the data
X = X[:-forecast_out] # X is first ninety percent of data
df.dropna(inplace = True)
y = np.array(df['label']) # labels based on features

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size = 0.2, random_state = 0)

'''
clf = LinearRegression(n_jobs = 32)
clf.fit(X_train, y_train) # training step
with open('linearregression.pickle' , 'wb') as f:
	pickle.dump(clf, f) # dump classifier into file as binary
'''
 # do not need to train classifier every time
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately)

#print(forecast_set, accuracy, forecast_out)

# all the values in the past do not have a forecast
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
	next_date = datetime.datetime.fromtimestamp(next_unix)
	next_unix += one_day
	# set all the info besides the forecast to not a number because that is in the future
	df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

# .loc work on index, .iloc work on position (identify using the actual value for example, the date)
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()
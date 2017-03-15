import sqlite3
import time
import random
import datetime
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from matplotlib import style

style.use('seaborn')


conn = sqlite3.connect('tutorial.db') # creates the database if it does not exist
c = conn.cursor()

def create_table():
	# all CAPS for SQLite commands, lowercase for what we are creating (do not actually need to capitalize, but a convention)
	c.execute('CREATE TABLE IF NOT EXISTS infoToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
# c is cursor, executes actions
# conn is the connection to the SQL database
def data_entry():
	c.execute("INSERT INTO infoToPlot VALUES(898123123, '2017-02-04', 'Python', 96)")
	conn.commit()
	c.close()
	conn.close()


def dynamic_data_entry():
	unix = time.time()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'Python'
	value = int(random.randrange(0,100))
	c.execute("INSERT INTO infoToPlot (unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)",
		(unix, date, keyword, value))
	conn.commit()

def read_from_db():
	c.execute("SELECT keyword, datestamp FROM infoToPlot WHERE (value = 9 OR value = 42) AND keyword = 'Python'")
	for row in c.fetchall():
		print(row)

def graph_data():
	c.execute("SELECT unix, value FROM infoToPlot")
	dates = []
	values = []
	for row in c.fetchall():
		print(row)
		dates.append(datetime.datetime.fromtimestamp(row[0]))
		values.append(row[1])
	plt.plot_date(dates, values, '-')
	plt.show()
#create_table()
#data_entry()
'''
for i in range(10):
	dynamic_data_entry()
	time.sleep(1)
'''
#read_from_db()

graph_data()
c.close()
conn.close



import sqlite3

conn = sqlite3.connect('tutorial.db') # creates the database if it does not exist
c = conn.cursor()

def create_table():
	# all CAPS for SQLite commands, lowercase for what we are creating (do not actually need to capitalize, but a convention)
	c.execute('CREATE TABLE IF NOT EXISTS infoToPlot(unix REAL, datastamp TEXT, keyword TEXT, value REAL)')

def data_entry():
	c.execute("INSERT INTO infoToPlot VALUES(898123123, '2017-02-04', 'Python', 96)")
	conn.commit()
	c.close()
	conn.close()

create_table()
data_entry()
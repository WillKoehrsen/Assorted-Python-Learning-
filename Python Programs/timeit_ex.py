import time
import datetime
import timeit

start_time = time.time()

print(datetime.datetime.fromtimestamp(start_time))

input_list = range(100)

print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
	if num%5 == 0:
		return True
	else:
		return False

xyz = [i for i in input_list if div_by_five(i)]''', number = 5000))

# number is number of executions, default is One million (main code run through One million times)
# time it with ''' triple quotes ''' around the statement and alter the number of executions
# xyz = [i for i in input_list if div_by_five(i)]
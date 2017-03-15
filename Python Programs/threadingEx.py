import threading
from queue import Queue
import time

print_lock = threading.Lock()

# Create the queue: list of tasks to be done
q = Queue()

# 20 jobs assigned, put the jobs on the queue
for worker in range(20):
	q.put(worker)


def exampleJob(worker):
	# Pretend to do work
	time.sleep(2)
	with print_lock:
		print(threading.current_thread().name, worker)

# The threader thread pulls a worker from the queue and processes it
def threader():
	while True:
		# get a worker from the queue
		worker = q.get()

		# Run the example job with the available worker in queue
		exampleJob(worker)

		# Completed with the job
		q.task_done()

# Number of threads
for x in range(10):
	t = threading.Thread(target = threader)
	# Classify as a daemon so the thread will die when the main thread dies
	t.daemon = True

	# Begins
	t.start()


start = time.time()


# Wait until the thread terminates put the worker back on the queue when finished
q.join()

# With 10 workers and 20 tasks, then the completed job should take 4 seconds
# Without threading, the job would take 40 seconds
print('Entire job took: ', time.time() - start)


#20 tasks to do with 10 threads (workers). Each worker will complete 2 tasks
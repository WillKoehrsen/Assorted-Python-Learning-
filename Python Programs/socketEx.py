import socket
import threading
from queue import Queue

print_lock = threading.Lock()

#AF_INET family, SOCK_STREAM type of socket
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = 'pythonprogramming.net'

def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try: 
		con = s.connect((target, port))
		with print_lock:
			print('port', port, 'is open!')

		con.close()
	except:
		pass

def threader():
	while True:
		# get the worker from the queue
		worker = q.get()
		# run the job with the worker
		portscan(worker) # each worker is a port in this example
		q.task_done()

q = Queue()

for x in range(256):
	t = threading.Thread(target = threader)
	t.daemon = True # each thread is a daemon that dies when the main thread dies as well
	t.start()

# 0 is an invalid port
for worker in range(1,1024): 
	q.put(worker) # put the worker to work

# wait until the worker is finished and then place back on queue
q.join()

'''
# port scanner: checks to see what ports are open (relatively slow)
def pscan(port):
	try:
		s.connect((server, port)) 
		return True
	except:
		return False

for x in range(1,26):
	if pscan(x):
		print('Port', x, 'is open')
	else:
		print('Port',x, 'is closed')

'''

# act like a browser
#port = 80

# get IP address of server
'''
server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"


s.send(request.encode())

# buffer: the amount of data downloaded at any moment
result = s.recv(4096)
# print(result)

while (len(result) > 0):
	print(result)
	result = s.recv(1024)
'''
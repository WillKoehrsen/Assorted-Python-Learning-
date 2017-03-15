import multiprocessing

def spawn(num, num2):
	print('Spawned whatever that means! {} {}'.format(num, num2))

if __name__ == "__main__":  # prevents program from running if imported 
	for i in range(8):
		p = multiprocessing.Process(target = spawn, args = (i,i+1))
		p.start()
		p.join()
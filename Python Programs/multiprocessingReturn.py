from multiprocessing import Pool 

# pool allows us to create a pool of workers

def job(num):
	return num / 2


if __name__=="__main__":
	p = Pool(processes = 2)
	print(type(p))
	data = p.map(job, range(20))
	data = p.map(job, range(25))
	p.close()
	print(data)
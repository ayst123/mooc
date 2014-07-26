from multiprocessing import Pool

def ina(num):
	a = []
	print "i am in a"
	a.append(num)
	if num == 2:
		a.append(22)
	return a

if __name__=='__main__':
	a = []
	pool = Pool()
	results = []
	input = [34,2,5]
	for i in range(len(input)):
		msg = input[i]
		results.append(pool.apply_async(ina,(msg,)))
	pool.close()
	pool.join()
	for res in results:
		a += res.get()
		print res.get()
	print a
			

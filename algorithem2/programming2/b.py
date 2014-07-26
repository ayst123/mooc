import urllib2
import uf
from multiprocessing import Pool

url = 'http://spark-public.s3.amazonaws.com/algo2/datasets/clustering_big.txt'
response = urllib2.urlopen(url)
data = response.read()

data = data.split('\n')
tolnum, bitnum = data[0].split(' ')
tolnum, bitnum = int(tolnum),int(bitnum)
data = data[1:-1]
#data = [''.join(x.split()) for x in data]
data = [x.split()[:bitnum] for x in data]
data = [[int(item) for item in x] for x in data]
print len(data)


#tolnum = 15
#bitnum = 8
#data = ['11001000','00111111','10101001','00100110','10101110','11011011',\
#	'10100111','11100100','00000001','01000110','11000000','10010110',\
#        '00111110','00101011','00011110']
#

def getpairs(ind):
	pairs = []
	item = data[ind]
	print ind
	
	if item in data[ind+1:]:
		index = data.index(item)
		pairs.append([ind,index])
		
	# find one different bit 
	for bitind in range(bitnum):
		temp = [x for x in item]
		temp[bitind] = 1-temp[bitind]
		if temp in data[ind+1:]:
		#	print 'first'
			index = data.index(temp)
			pairs.append([ind,index])

	# find two different bits
	for bit1 in range(bitnum):
		for bit2 in range(bit1+1,bitnum):
			temp = [x for x in item]
			temp[bit1] = 1-temp[bit1]
			temp[bit2] = 1-temp[bit2]
			if temp in data[ind+1:]:
				#print 'second'
				index = data.index(temp)
				pairs.append([ind,index])
	
	return pairs

if __name__=='__main__':
	pairs = []
	result = []
	
	pool = Pool()
	for ind in range(len(data)):
		result.append(pool.apply_async(getpairs,(ind,))) 	
	pool.close()
	pool.join()
	for res in result:
		pairs += res.get()

	clus = uf.uf(tolnum)
	for item in pairs:
		clus.union(item[0],item[1])
	
 	print 'clus count: ',clus.count()	
			
		

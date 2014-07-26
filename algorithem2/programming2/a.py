import urllib2
import uf

url = 'http://spark-public.s3.amazonaws.com/algo2/datasets/clustering1.txt'
response = urllib2.urlopen(url)
data = response.read()

data = data.split('\n')
tolnum = int(data[0])
data = data[1:-1]
data = [x.split(' ') for x in data]
data = [ [ int(x[0]),int(x[1]),int(x[2])  ] for x in data]

tolnum = 4
data = [[1,2,10],[1,3,11],[1,4,2],[2,3,1],[2,4,8],[3,4,12]]
clus = uf.uf(tolnum)
while (clus.count()>2):
	print clus.count()
	mindis = float('infinity')
 	minid = 0
	for ind,item in enumerate(data):
		if not clus.connected(item[0]-1,item[1]-1):
			if item[2]<mindis:
				mindis = item[2]
  				minid = ind
	clus.union(data[minid][0]-1,data[minid][1]-1)
	print minid,mindis
	
print clus.count()
print minid, mindis
print clus.id

	
			

	
	


import urllib2

url = 'http://spark-public.s3.amazonaws.com/algo2/datasets/edges.txt'
response = urllib2.urlopen(url)
data = response.read()

data = data.split('\n')
temp = data[0].split(' ')
tolver = int(temp[0])
toledges = int(temp[1])
data = data[1:-1]
data = [x.split(' ') for x in data]
data = [ [ int(x[0]),int(x[1]),int(x[2])  ] for x in data]

#tolver = 4
#toledges = 6
#data = [[1,2,5],[2,3,-4],[4,3,3],[1,4,2],[1,3,1]]

temp = [[] for i in range(tolver)]
vertices = range(1,tolver+1)
dicver = dict(zip(vertices,temp))
for item in data:
	dicver[item[0]].append([item[1],item[2]])
	dicver[item[1]].append([item[0],item[2]])

cur_vers = [1]
trees = []
cost = 0
for i in range(tolver-1):
	print len(cur_vers)
	min_cost = float('infinity')
	min_item = [1,1,1] 
	for ver in cur_vers:
		templist = dicver[ver]
		for neighbor in templist:
			if neighbor[0] not in cur_vers:
		#		print ver,neighbor
				if neighbor[1]<min_cost:
					min_cost = neighbor[1]
					min_item[0]= ver
					min_item[1]= neighbor[0]
					min_item[2]= neighbor[1]
	cur_vers.append(min_item[1])
	trees.append(min_item)
	cost += min_item[2]

print '----final result----'
print len(cur_vers)
print len(trees)
print cost


	
		
		
	
	
	





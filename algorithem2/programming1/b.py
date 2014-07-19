import urllib2

url = 'http://spark-public.s3.amazonaws.com/algo2/datasets/jobs.txt'
response = urllib2.urlopen(url)
data = response.read()

data = data.split('\n')
data = data[1:-1]
data = [x.split(' ') for x in data]
data = [ [ float(x[0]),float(x[1])  ] for x in data]

# deal with data
temp = [[] for x in data]
ratio = [x[0]/x[1] for x in data]
dic = dict(zip(ratio,temp))

for ind,item in enumerate(data):
	dic[ratio[ind]].append(item)


ratio_keys = sorted(dic.keys(),reverse=True)
wlen = 0
len = 0
for ratio_item in ratio_keys:
   	for item in dic[ratio_item]:
		len += item[1]
		wlen += item[0] * len
			
print len,wlen


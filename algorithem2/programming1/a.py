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
diff = [x[0]-x[1] for x in data]
dic = dict(zip(diff,temp))

for ind,item in enumerate(data):
	dic[diff[ind]].append(item)


diff_keys = sorted(dic.keys(),reverse=True)
wlen = 0
len = 0
for diff_item in diff_keys:
	cur_list = dic[diff_item]
	cur_w = [x[0] for x in cur_list]
 	cur_l = [x[1] for x in cur_list]
 	cur_dic = dict(zip(cur_w,cur_l))
  	cur_w = sorted(cur_w,reverse=True)
 
   	for item in cur_w:
		len += cur_dic[item]
		wlen += item * len
			
print len,wlen


class uf:
	def __init__(self,n):
		self.id = range(n)
		self.sz = [1]*n

	def count(self):
		counter = 0
		for ind,p in enumerate(self.id):
			if ind == self.id[p]:
				counter += 1		
		return counter

	def connected(self,p,q):
		return self.find(p)==self.find(q)
	
	def find(self,p):
		while p!= self.id[p]:
			self.id[p] = self.id[self.id[p]]
			p = self.id[p]
		return p

	def union(self,p,q):
		pid,qid = self.find(p),self.find(q)
		if pid == qid: return
		
		if self.sz[pid]<self.sz[qid]:
			self.id[pid] = qid
			self.sz[qid] += self.sz[pid]
		else:
			self.id[qid] = pid
			self.sz[pid] += self.sz[qid]
		

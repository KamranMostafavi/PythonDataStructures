from heapq import _siftdown
class PQueue:
	
   	def __init__(self, maxSize):
   		self.size = 0
   		self.maxSize = maxSize
   		self.H = [0 for j in range(maxSize)]		
	
	def Parent(self, i):
		return (i/2)
		if i==1:
			return -1
		else:
			return (i/2)
	
	def LeftChild (self,i):
		return (2*i)
		if (2*i) > self.size:
			return -1
		else:
			return (2*i)

	def RightChild (self,i):
		return ((2*i)+1)
		if (2*i)+1 > self.size:
			return -1
		else:
			return ((2*i)+1)
		
	def CopyArray(self,a):
		self.H = a
		self.size=len(a)
		
	def SiftUp(self,i):
		print ("sift up:", i)
		while i > 1 and self.H[self.Parent(i)-1] < self.H[i-1]:
			print ("swap: ", i, self.Parent(i))
			temp=self.H[self.Parent(i)-1]
			self.H[self.Parent(i)-1]=self.H[i-1]
			self.H[i-1]=temp
			i=self.Parent(i)
			
	def	Insert(self, p):
		if self.size == self.maxSize:
			return False
		self.size=self.size+1
		self.H[self.size-1]=p
		self.SiftUp(self.size)
	
	def SiftDown(self,i):
		print ("sift down:", i)
		maxIndex=i
		l=self.LeftChild(i)
		if l <= self.size and self.H[l-1] > self.H[maxIndex-1]:
			maxIndex = l
		r=self.RightChild(i)
		if r<= self.size and self.H[r-1]>self.H[maxIndex-1]:
			maxIndex = r
		if i != maxIndex:
			print ("swap: ", i, maxIndex)
			temp=self.H[i-1]
			self.H[i-1] = self.H[maxIndex-1]
			self.H[maxIndex-1]=temp
			self.SiftDown(maxIndex)

	def	ExtractMax(self):
		result=self.H[1-1]
		self.H[1-1]=self.H[self.size-1]
		self.size=self.size-1
		self.SiftDown(1)
		return result		

	def Remove(self,i):
		result=self.H[i-1]
		self.H[i-1]=self.H[0]+1	#make element one higher than root
		self.SiftUp(i)
		self.ExtractMax()
		return result
	
	def ChangePriority(self,i,p):
		oldp=self.H[i-1]
		self.H[i-1]=p
		if p > oldp:
			self.SiftUp(i)
		else:
			self.SiftDown(i)
	
	def	BuildHeap(self,a):
		self.CopyArray(a)
		for i in range (self.size/2, 0, -1):
			self.SiftDown(i)
						
	def HeapSort(self,a):
		self.BuildHeap(a)
		#print ("start:", self.H)
		n=size=self.size
		for i in range (n-1):
			temp=a[1-1]
			a[1-1]=a[self.size-1]
			a[self.size-1]=temp
			self.size=self.size-1
			#print (i, self.H)
			self.SiftDown(1)
			#print (":",i, self.size, self.H)
		
		self.size=size	#restore size of the array
			
if __name__ == "__main__":
	
	a=[29,18,49,14,18,7,13,11,12]

	pq=PQueue(20)
	
	#pq.CopyArray(a)
	
	
	pq.Insert(18)
	pq.Insert(7)
	pq.Insert(18)
	pq.Insert(42)
	pq.Insert(11)
	pq.Insert(13)
	pq.Insert(29)
	pq.Insert(12)
	pq.Insert(14)
	
	
	
	
	print (pq.H)
	
	for i in range (1, pq.size+1):
		print (i, pq.H[i-1], pq.Parent(i), pq.LeftChild(i), pq.RightChild(i))

	
	print ("removed: %d " % pq.Remove(5))
	print (pq.H)
	
	pq.ChangePriority(5, 33)
	print (pq.H)
	
	while pq.size > 0:
		print (pq.ExtractMax())
	

	pq.BuildHeap(a)
	print (pq.H)
	for i in range (1, pq.size+1):
		print (i, pq.H[i-1], pq.Parent(i), pq.LeftChild(i), pq.RightChild(i))
	
	
	while pq.size > 0:
		print (pq.ExtractMax())
	
	a=[29,18,49,14,18,7,13,11,12]
	print (a)
	pq=PQueue(20)	
	pq.HeapSort(a)
	print (pq.size, pq.H)
	
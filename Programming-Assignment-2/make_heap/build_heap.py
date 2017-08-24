# python3
'''
  in this assignment one converts an array of integers into a minimal heap. in a
  minimal heap, the key of node is less than its left and right children.

  assignment details: file:///C:/Users/Kamran/Documents/eduction/data%20structures/Programming-Assignment-2/Programming-Assignment-2.pdf

  input:
    the first line indicates the number of integers in the array
    the next line is a space separated list of integers

  output:
    print number of swaps necessary to convert the array into a minimal heap
    print each swap in a line
    
  processing:
    nodes are numbered starting with 1, note node 1 corresponds to index 0 in
    the array holding the keys (integers in this case).
    
'''
class HeapBuilder:
  def __init__(self):
    self._swaps = []  #array holding the swaps
    self._data = []   #array holding the keys (integers)
    self.size = int(len(self._data))

  def Parent(self, i):
    #i is the node number (1..n) 
    return (i/2)

  def LeftChild (self,i):
    return (2*i)

  def RightChild (self,i):
    return ((2*i)+1)

  def BuildHeap(self):
    for i in range (int(self.size/2), 0, -1):
      self.SiftDown(i)

  def SiftDown(self,i):
    print ("sift down:", i-1) #note nodes are 1 based for purposes of calculating left and right child but array is zero based
    maxIndex=i
    l=self.LeftChild(i)
    if l <= self.size and self._data[l-1] < self._data[maxIndex-1]:
      maxIndex = l
    r=self.RightChild(i)
    if r <= self.size and self._data[r-1] < self._data[maxIndex-1]:
      maxIndex = r
    if i != maxIndex:
      temp=self._data[i-1]
      self._data[i-1] = self._data[maxIndex-1]
      self._data[maxIndex-1]=temp
      self._swaps.append((i-1, maxIndex-1))
      print ("swapping:", self._data[i-1], self._data[maxIndex-1])
      print (self._swaps)
      self.SiftDown(maxIndex)

  def ReadData(self):
    self._swaps = []
    self._data = []
    self.size = int(len(self._data))
    '''
    f = open ('tests/05.txt')
    n = int(f.readline())
    self._data = [int(s) for s in f.read().split()]
    print (n)
    print (self._data)
    '''
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)
    self.size=n

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def Solve(self):
    '''
    self.ReadData()
    print ("original 1:",self._data)
    self.GenerateSwaps()
    print ("processed 1:",self._data)
    self.WriteResponse()
    '''
    self.ReadData()
    #print ("original 2:",self._data)
    self.BuildHeap()
    #print ("processed 2:",self._data)
    self.WriteResponse()
    
if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

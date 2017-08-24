# python3
'''
  exercise in inorder, preorder and postorder traversal of a tree.
  inorder traversal is the code that is executed in between recursive calls to left and right children
  preorder traversal is the code that is executed prior to recursive calls to left and right children
  postorder traversal is the code that is executed after the recursive calls to left and right children
  
'''
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline()) #read number of nodes in tree
    self.key = [0 for i in range(self.n)] #init keys list
    self.left = [0 for i in range(self.n)] #init left_pointer list
    self.right = [0 for i in range(self.n)] #init right_pointer list
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())  #read key, left_pointer, right_pointer
      self.key[i] = a     #populate the lists accordingly
      self.left[i] = b
      self.right[i] = c
    #print (self.key)
    #print (self.left)
    #print (self.right)

  def inOrder(self,i):
    '''
    if tree=Nil
      return
    inOrder(tree.left)
    print(tree.key)
    inOrder(tree.right)
    '''

    # Finish the implementation
    # You may need to add a new recursive method to do that
    #print ("node: ",i)
    if i==-1:
      return self.result
    if i==0:
      self.result = [] #holds list of keys in some order
    '''  
    if self.left[i] == -1 and self.right[i]== -1:
      self.result.append(self.key[i])
      return self.result
    '''
    self.inOrder(self.left[i])
    self.result.append(self.key[i])
    self.inOrder(self.right[i])
    return self.result

  def preOrder(self,i):
    '''
    if tree=Nil
      return
    print (tree.key)  
    preOrder(tree.left)
    preOrder(tree.right)
    '''

    # Finish the implementation
    # You may need to add a new recursive method to do that
    #print ("node: ",i)
    if i==-1:
      return self.result
    if i==0:
      self.result = [] #holds list of keys in some order
    '''
    if self.left[i] == -1 and self.right[i]== -1:
      self.result.append(self.key[i])
      return self.result
    '''
    self.result.append(self.key[i])
    self.preOrder(self.left[i])
    self.preOrder(self.right[i])
    return self.result

  
  def postOrder(self,i): #create list of keys postOrder
    '''
    if tree=Nil
      return
    postOrder(tree.left)
    postOrder(tree.right)
    print (tree.key)
    '''

    # Finish the implementation
    # You may need to add a new recursive method to do that
    #print ("node: ",i)
    if i==-1:
      return self.result
    if i==0:
      self.result = [] #holds list of keys in some order
    '''
    if self.left[i] == -1 and self.right[i]== -1:
      self.result.append(self.key[i])
      return self.result
    '''
    self.postOrder(self.left[i])
    self.postOrder(self.right[i])
    self.result.append(self.key[i])
    return self.result
  
def main():
	tree = TreeOrders() #create object
	tree.read() #read input
	print(" ".join(str(x) for x in tree.inOrder(0))) #print inOrder
	print(" ".join(str(x) for x in tree.preOrder(0))) #print preOrder
	print(" ".join(str(x) for x in tree.postOrder(0))) #print postOrder

threading.Thread(target=main).start()

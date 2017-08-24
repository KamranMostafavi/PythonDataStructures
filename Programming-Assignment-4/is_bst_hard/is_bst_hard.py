#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class isBSTObj:
  def __init__(self, tree):
    self.BstStatus=True         #holds the status of bst
    self.tree=tree
    self.max=None
    self.min=None
    self.sortedlist=[]
    self.rightChildren=[]

  def leftChild(self, i):
    return self.tree[i][1]

  def rightChild(self, i):
    return self.tree[i][2]

  def nodeValue(self, i):
    return self.tree[i][0]

  def rootValue(self):
    return self.nodeValue(0)
  
  def isRightChild(self,i, p):
    if i == -1 or p == -1:
      return False
    if i == self.rightChild(p):
      return True
    elif self.nodeValue(i) != self.nodeValue(p) and self.nodeValue(i) >= self.rootValue():
      return True
    else:
      return False 

  def isLeftChild(self, i, p):
    if i == -1 or p == -1:
      return False
    if i == self.leftChild(p):
      return True
    else:
      return False     

  def IsBinarySearchTree(self, i):
    '''
      if BstStatus == False return
      if tree is nil (-1) return
      IsBinarySearchTree(leftChild)
      evaluate if the nodes are in ascending order, if not set BstStatus to False
      IsBinarySearchTree(rightChild)
      return BstStatus
    '''
    if len(self.tree) == 0:
      return self.BstStatus
    if self.BstStatus == False:
      return self.BstStatus
    if i == -1:
      return self.BstStatus

    self.IsBinarySearchTree(self.rightChild(i))
    if i != -1:
      if len(self.sortedlist) == 0:
        self.sortedlist.append([i, self.nodeValue(i)])
      elif self.nodeValue(i)< self.sortedlist[len(self.sortedlist)-1][1]:
        # if i is a rightchild then it is OK
        self.sortedlist.append([i,self.nodeValue(i)])
      elif self.nodeValue(i)> self.sortedlist[len(self.sortedlist)-1][1]:
        self.BstStatus=False
        return self.BstStatus        
      elif self.nodeValue(i) == self.sortedlist[len(self.sortedlist)-1][1] and self.isLeftChild(i, self.sortedlist[len(self.sortedlist)-1][0]):
        self.BstStatus=False
        return self.BstStatus
      else:
        self.sortedlist.append([i,self.nodeValue(i)])
    #print (self.nodeValue(i))    
    self.IsBinarySearchTree(self.leftChild(i))
    return self.BstStatus

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    # read each line as a list and store it in tree - tree is a list of lists
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  #print (tree)

  bst=isBSTObj(tree)
  
  if bst.IsBinarySearchTree(0):
    print("CORRECT")
  else:
    print("INCORRECT")

  #print (bst.sortedlist)

threading.Thread(target=main).start()

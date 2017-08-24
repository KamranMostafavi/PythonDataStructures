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

  def leftChild(self, i):
    return self.tree[i][1]

  def rightChild(self, i):
    return self.tree[i][2]

  def nodeValue(self, i):
    return self.tree[i][0]

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

    self.IsBinarySearchTree(self.leftChild(i))
    if (len(self.sortedlist) == 0):
      self.sortedlist.append(self.nodeValue(i))
    elif self.nodeValue(i)>self.sortedlist[len(self.sortedlist)-1]:
      self.sortedlist.append(self.nodeValue(i))
    else:
      self.BstStatus=False
      return self.BstStatus
    #print (self.nodeValue(i))    
    self.IsBinarySearchTree(self.rightChild(i))
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

threading.Thread(target=main).start()

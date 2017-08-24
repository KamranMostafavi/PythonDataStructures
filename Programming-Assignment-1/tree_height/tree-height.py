# python3
'''
        in this example, the maximum height of a tree is returned.
        input:
                first line contains number of nodes in the tree
                remaining lines contain the parent of a node or -1 if the node
                has no parents and is the root
        output:
                returns max height of the tree (only one node in the tree returns 1)
                file:///C:/Users/Kamran/Documents/eduction/data%20structures/Programming-Assignment-1/Programming-Assignment-1.pdf
'''
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline()) #no of nodes in the tree
                self.parent = list(map(int, sys.stdin.readline().split())) #each cell contains node's parent
                self.depth=[0 for _ in range(len(self.parent))] #each cell contains node's depth or height (1 based, ie: root has depth of 1)

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n): #walk the tree for each node/vertex back to root and compute its height/depth
                        height = 0
                        i = vertex
                        while i != -1:
                            height += 1
                            j=i
                            i = self.parent[i]
                            #print (j,i, height)
                            if self.depth[i]!=0:
                                height=height+self.depth[i]
                                #self.depth[vertex]=height
                                #print ("depth of %d is %d" %(j, height)) 
                                break;
                        self.depth[vertex]=height
                        #print ("dept %d = %d" %(vertex, self.depth[vertex]))
                        maxHeight = max(maxHeight, height);
                return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  #print (tree.parent)
  print(tree.compute_height())
  #print (tree.depth)

threading.Thread(target=main).start()

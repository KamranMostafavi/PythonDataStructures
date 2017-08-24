# python3

import sys
'''
Task.
    There are n tables stored in some database. The tables are numbered from 1 to n.
    All tables share the same set of columns. Each table contains either several rows with real data
    or a symbolic link to another table. Initially, all tables contain data, and i-th table has r_i rows.
    You need to perform m of the following operations:
    1. Consider table number destination i. Traverse the path of symbolic links to get to the data.
    That is, while destination i contains a symbolic link instead of real data do destination_i = symlink(destination_i)
    2. Consider the table number source_i and traverse the path of symbolic links from it in the same manner as for destination_i.
    3. Now, destination_i and source_i are the numbers of two tables with real data. If destination_i= source_i, copy all the rows
    from table source_i to table destination_i, then clear the table source_i and instead of real data put a symbolic link to destination_i
    into it.
    4. Print the maximum size among all n tables (recall that size is the number of rows in the table). If the table contains only a symbolic link,
    its size is considered to be 0. See examples and explanations for further clarifications.
    Input Format.
        The first line of the input contains two integers n and m the number of tables in the database and the number of merge queries to perform, respectively.
        The second line of the input contains n integers r_i the number of rows in the i-th table. Then follow m lines describing merge queries. Each of them
        contains two integers destination_i and source_i the numbers of the tables to merge.

    Output Format. For each query print a line containing a single integer the maximum of the sizes of all tables (in terms of the number of rows) after
    the corresponding operation.

example:
    input:
        5 5
        1 1 1 1 1
        3 5
        2 4
        1 4
        5 4
        5 3 
        
    output:
       2
       2
       3
       5
       5 
'''
class disjointSet:
    def __init__(self, size, lines):
        self.size=size
        self.rank=[0]*size
        self.parent= list(range(1,size+1))
        self.lines=lines
        self.maxval=max(lines)
                          
    def Find(self,i):
        while i != self.parent[i-1]:
            i= self.parent[i-1]
        return i


    def betterFind(self, i):
        #This does path compression which in effect reduces the height of the set (which is a tree)
        if i != self.parent[i-1]:
            self.parent[i-1] = self.betterFind(self.parent[i-1])
        return self.parent[i-1]
                          
    def Union(self,j,i):
        #This union puts a set with samller rank under the other set. If the ranks of the two sets are equal then the rank of the resulting set is one greater.
        i_id=self.betterFind(i)
        j_id=self.betterFind(j)
        if i_id == j_id:
            return
        if self.rank[i_id-1] > self.rank[j_id-1]:
            self.parent[j_id-1]=i_id #merge set with lower depth to set with higher depth
            self.lines[i_id-1]=self.lines[i_id-1]+self.lines[j_id-1] 
            self.lines[j_id-1]=0  #symbolic link is added (size of 0) and no.of.records(or lines) is added to the parent set
            if self.lines[i_id-1] > self.maxval:
                self.maxval=self.lines[i_id-1]
        else:
            self.parent[i_id-1]=j_id
            p_id=j_id
            if self.rank [i_id-1]== self.rank[j_id-1]:    
                self.rank[j_id-1]=self.rank[j_id-1]+1  #increment rank of the set id if the two sets were of equal depth
            self.lines[j_id-1]=self.lines[j_id-1]+self.lines[i_id-1]
            self.lines[i_id-1]=0
            if self.lines[j_id-1] > self.maxval:
                self.maxval=self.lines[j_id-1]
        #print ("Union", j,i,j_id,i_id,p_id,self.lines[p_id-1],self.lines[i-1])

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(1, n+1)) #creates a list/array [0,1,....,n-1]
ans = max(lines) #returns max number of rows of all tables

myset=disjointSet(n,lines)
#print (myset.parent)
#print (myset.rank)
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    #print (destination, source)
    myset.Union(destination, source)
    #print (myset.parent)
    #print (myset.rank)
    #print (myset.lines)
    print (myset.maxval)


'''                          
def getParent(table):
    # find parent and compress path
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    return True

                          
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
'''    

# python3

class Query:
    '''
    input:
    m  
    n
    query 1
    query 2
    etc

    m=size of the hash table
    n=number of querries to read

    queries are as follows:
    add string
    del string
    find string
    check i 

    example:
    input:
    5
    12
    add world
    add HellO
    check 4
    find World
    find world
    del world
    check 4
    del HellO
    add luck
    add GooD
    check 2
    del good

    output:
    HellO world
    no
    yes
    HellO
    GooD luck

    explanation:
        4 is the hash for "world" and "Hello", hence "check 4" returns "HellO world". Same is true for "check 2", returning "GooD luck".
        since hash of "World" and "world" are different and "World" was not added to the table, "find World" returns "no". "del good" returns
        a blank line as "good" is not in the table.

        hashing reduces the amount of memory needed to store elements, while keeping the access operations relatively fast. If elements share
        a hash,then they are stored in a first in first out queue (ex: HellO and world)
   
    '''

    def __init__(self, query):
        '''
        query object
            self.ind is the index into the hash table
            self.s is the string stored in the hash table.
            self.type is the query: find, del, add, and check

            query is a list example: [find, world] or [check, 4] etc.
        '''
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in this hash table. each element is either 0 or a list containing the string(s) with the same hash number
        self.elems = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))      #if chain is ['hello', 'world'] then the resulting string to be printed is 'hello world' (ie: 'hello'+' '+'world')
 
    def read_query(self):           #returns a query object drived from input
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems[query.ind]))
        else:
            if query.type == 'find':
                if self.elems[self._hash_func(query.s)].count(query.s) == 0:
                    self.write_search_result(False)
                else:
                    self.write_search_result(True)
                    
            elif query.type == 'add':
                if self.elems[self._hash_func(query.s)].count(query.s) == 0:
                    self.elems[self._hash_func(query.s)].append(query.s)
            else:   # here if del
                try:
                    self.elems[self._hash_func(query.s)].remove(query.s) #throws ValueError id string does not exist , catch exception
                except ValueError:
                    pass      #ignore if the string does not exist
    '''
    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)
    '''
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

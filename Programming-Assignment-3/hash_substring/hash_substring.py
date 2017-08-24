# python3
from math import pow
from random import randint
'''
    implements Rabin Karp Algorithm in order search a pattern in a string and output all occurrences of it.
    Rabin Karp algoritm run time without precomputing the hashes is O(|T|*|P|). However with precomputation
    it is improved to O(|T|+|P|).
    
    example:

    input:
    aba
    abacaba

    output:
    0 4
    
'''
class RabinKarpObj:

    def __init__(self):
        self._prime = 1000000007
        self._multiplier = 300
    
    def PolyHash(self, s):
            hsh = 0
            for i in range (len(s)-1, -1, -1):
                hsh = (hsh * self._multiplier + ord(s[i])) % self._prime
            return hsh

    def AreEqual(self, s1, s2):
        if len(s1) != len (s2):
            return False
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                return False
        return True
  
    '''
    def PrecomputeHashes(self, T, sizeofP):
        H = [0 for _ in range (len(T)-sizeofP + 1)]
        for i in range(len(T)-sizeofP+1):
            H[i]=self.PolyHash(T[i:i+sizeofP])
            #print ("Hash for ", T[i:i+sizeofP], " is ", H[i])
        return H
    '''
    
    
    def PrecomputeHashes(self, T, sizeofP):
        #precomputes hashes for substring that are the same length as pattern starting from end of Text string going back
        #the list of hashes are returned
        H = [0 for _ in range (len(T)- sizeofP + 1)]
        S = T[len(T)-sizeofP:]
        H[len(T)-sizeofP]=self.PolyHash(S)  
        #print ("S : ", S, " Hash: ", H[len(H)-sizeofP])
        y=1
        for i in range(0, sizeofP):
            y=(y*self._multiplier) % self._prime
        for i in range (len(T)-sizeofP-1, -1, -1):  #start from end of Text String - size of pattern and go back
            H[i]=(self._multiplier*H[i+1]+ ord(T[i]) - y*ord(T[i+sizeofP])) % self._prime  #hash of substring [i..j] is a function of substring [i-1..j-1]
            #H[i]=self.PolyHash(T[i:i+sizeofP])
            #print (sizeofP, i,H[i], H[i+1], T[i], ord(T[i]), y, ord(T[i+sizeofP]), T[i:i+sizeofP])
        #print (H)
        return H
    

        
    def RabinKarp(self, T, P):
        result = []
        sizeofP = len(P)
        pHash = self.PolyHash(P)
        #print ("Multiplier is: ", self._multiplier)
        #print ("Hash of pattern is:",pHash)
        H=self.PrecomputeHashes(T, sizeofP)
        #print (len (T), len (P))
        #print (len(H),H)
        for i in range (0, (len(T) - sizeofP) + 1):
            #print (i)
            if pHash != H[i]:
                continue
            #print ("found a match at ", i, T[i:i+sizeofP])
            if T[i:i+sizeofP]==P:
                result.append(i)
        return result
        
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):  #output is a list
    #print (output)
    print(' '.join(map(str, output))) #converts a list of integer values to strings 

def get_occurrences(pattern, text):
    #print ("T:", text)
    #print ("P:", pattern)
    
    rk=RabinKarpObj()
    return  rk.RabinKarp(text, pattern)  

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


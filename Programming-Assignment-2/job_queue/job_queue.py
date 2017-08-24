# python3
'''
    Author: Kamran Mostafavi
    This is an example of a job queue for an operating system. Assume the operating
    system has n threads for processing m jobs.

    jobs are processed in a thread that is available. If more than one thread is available
    then the thread with lowest index processes the job. A thread must complete a job before
    it can process another. There is no pre-emption or job interruption.

    the program outputs for each job, the thread that processed it and the time it started processing it.

    The program builds a heap for threads. each thread has an index (0...n) and a rank which is the availability start time for the thread.
    for this to work, the heap needs to be minimal so the thread with the lowest available time slot is selected to perform the next job

    input:
        n   no of threads
        m   no of jobs
        t   time it takes for each job to be processed (for m jobs separated by space)
    output:
        thread_number start_time


    example:
        input:
        2 5
        1 2 3 4 5

        output:
        0 0
        1 0
        0 1
        1 2
        0 4

        in the example, 2 threads and 5 jobs are available

        time
        0    j1 is processed, rank(0)=1
        0    j2 is processed by thread 1, rank(1)=2
        1    J3 is processed by thread 0, rank(0)=1+3=4
        2    J4 is processed by thread 1, rank(1)=2+4=6
        4    J5 is processed by thread 0, rank(0)=4+5=9

        Note as rank increases, the thread gets closer to the leaves of the heap, allowing the thread that becomes available sooner to claim the next job in the
        queue.
         
'''
class JobQueue:
    
    class PQueue:
    
        def __init__(self, maxSize):
           self.size = 0
           self.maxSize = maxSize
           self.H = [0 for j in range(maxSize)]        
    
        def Parent(self, i):
            return int(i/2)
    
        def LeftChild (self,i):
            return int(2*i)

        def RightChild (self,i):
            return int((2*i)+1)

        def CopyArray(self,a):
            #not used
            self.H = a
            self.size=len(a)

        def CmpPriority(self,i, j):
            #this routine returns True if rank of node j is higher than node i
            #or when index of node j is higher than i if their ranks are equal
            #otherwise, it returns false
            i=int(i)
            j=int(j)
            if self.H[i-1].rank < self.H[j-1].rank:
                return True
            elif self.H[i-1].rank == self.H[j-1].rank:
                if self.H[i-1].index < self.H[j-1].index:
                    return True
                else:
                    return False
            else:
                return False
                
            
        def SiftUp(self,i):
            #note this is a minimal heap so if the rank of i is less than it's parent, then swaps happen
            while i > 1 and self.CmpPriority(i, self.Parent(i)):
                temp=self.H[self.Parent(i)-1]
                self.H[self.Parent(i)-1]=self.H[i-1]
                self.H[i-1]=temp
                i=self.Parent(i)
            
        def Insert(self, p):
            #inserts an object, thread into the heap
            if self.size == self.maxSize:
                return False
            self.size=self.size+1
            self.H[self.size-1]=p
            self.SiftUp(self.size)
    
        def SiftDown(self,i):
            maxIndex=i
            l=self.LeftChild(i)
            if l <= self.size and self.CmpPriority(l, maxIndex):
                maxIndex = l
            r=self.RightChild(i)
            if r<= self.size and self.CmpPriority(r, maxIndex):
                maxIndex = r

            # swaps happen if rank of node is greater than its children and it will happen with the child with the lower rank
            if i != maxIndex:
                temp=self.H[i-1]
                self.H[i-1] = self.H[maxIndex-1]
                self.H[maxIndex-1]=temp
                self.SiftDown(maxIndex)

    
        def ChangePriority(self,i,p):
            #if new priority is less than old priority for a given node, then want to siftUp, otherwise siftDown. Note priority is the time at which a given
            #thread is available.
            oldp=self.H[i-1].rank
            self.H[i-1].rank=p
            if p < oldp:
                self.SiftUp(i)
            else:
                self.SiftDown(i)

        def printpq(self):
            #index is thread id, rank is the time when thread becomes available to process the next job in the queue
            for e in self.H:
                print (e.index, e.rank)
    
    class thread:
        def __init__(self, index, rank):
            self.index=index
            self.rank=rank

    #a = sorted(a, key = lambda t: (t.rank,t.index))
    
    def read_data(self):
        self.num_workers, m = map(int, input().split())   #read no.of.threads and no.of.jobs
        self.jobs = list(map(int, input().split()))       #read processing time of each job
        assert m == len(self.jobs)                        #make sure correct no.of.jobs passed matches no.of.jobs
        self.workers=[]                                   #perhaps not necessary variable
        # build a priority heap for the threads
        self.pq=self.PQueue(self.num_workers)
        for i in range (self.num_workers):
            t=self.thread(i,0)                           #build a thread object (all ranks are zero initially)
            self.workers.append(t)          
            self.pq.Insert(t)                            #starts with an empty heap and builds it by inserting new thread objects while threads remain

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        #rank of the heap is the start time of job for a thread. Since the start time changes, one wants to process the job with the smallest
        #start time, hence the heap is minimal, meaning the root rank is less than or equal to its children
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)         #for each job, it contains the thread index that processed it
        self.start_times = [None] * len(self.jobs)              #for each job, it contains the start time of the job
        next_free_time = [0] * self.num_workers                 #not used

        for j in range (len(self.jobs)):
            self.assigned_workers[j]=self.pq.H[0].index             #root of the pq is the thread that processes next job
            self.start_times[j]=self.pq.H[0].rank                   #record start time of a job
            self.pq.ChangePriority(1,self.pq.H[0].rank+self.jobs[j]) #use processing time of job to determine new rank (when thread is available) and change the heap

    def solve(self):
        '''
            read input
            assign jobs to threads
            display output
        '''
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


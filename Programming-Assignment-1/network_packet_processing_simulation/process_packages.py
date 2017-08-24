# python3
import sys
'''
    Author: Kamran Mostafavi
    This models a network processor. The network processor can only handle one packet at a time. There is also a network
    buffer that queues the packets as they arrive, if the network buffer is full and packets arrive then they are dropped.
    Network buffer is implemented as a queue data structure (FIFO)

    input:
        first line contains the size of the input buffer and the number of packets that arrive
        each other line contains the the time or arriaval of a packet (Ai) and its processing time(Pi)
    output:
        for each packet print -1 if the packet was dropped or the time the packet was loaded into processor to be processed.


    example input:
        1 3       ;packet processing buff size=1, 3 packets to follow
        0 1       ;packet arrives at t=0 and takes 1 clk to be processed
        1 3       ;packet arrives at t=1 and takes 3 clks to be processed
        4 2       ;packet arrives at t=4 and takes 4 clks to be processed


    example output:
        0         ;1st packet is processed at t=0
        1         ;next packet is processed at t=1
        4         ;next packet is processed at t=4
                
    
'''
class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time
        
class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped            #boolean, True if packet is dropped
        self.start_time = start_time      #holds time when packet is loaded into the packet processor from buffer to be processed

class PackageProcessor:
    def __init__(self, size, count):
        self.size = size        #size of packet processing buffer
        self.finish_time= []    #holds finish time of request (packet) - this mimicks the packet input buffer
        self.ReadRequests(count) #start reading the packets

    def packetBufferEmpty(self):
        return (len(self.finish_time) == 0)

    def packetBufferFull(self):
        if self.packetBufferEmpty():
            return False
        if len(self.finish_time) >= self.size:
            return True
        else:
            return False

    def putPacketInBuffer(self,request):
        #compute finish time of the packet(request) and store it in buffer
        if self.packetBufferEmpty():
            start_time=request.arrival_time
        else:
            start_time=self.finish_time[len(self.finish_time)-1]
        self.finish_time.append(start_time+request.process_time)
        return start_time


    def removeProcessedPackets(self,request):
        #as each new packet arrives, remove a packet that was processed. note that the input buffer is a queue so the
        #packet at index 0 is removed (first in first out)
        if self.packetBufferEmpty():
            return
        elif request.arrival_time >= self.finish_time[0]:
            self.finish_time.pop(0)

    def Process(self, request):

        #before processing a packet remove packet that is already processed from input buffer 
        self.removeProcessedPackets(request)

        if self.packetBufferFull() and request.arrival_time < self.finish_time[self.size-1]:
            return Response(True, -1)    #if packet buffer is full and still packets to be processed then indicate packet is dropped
    
        elif request.process_time >=0:   #process the packet
            start_time=self.putPacketInBuffer(request)
            return Response(False, start_time)

    def ReadRequests(self,count):
    # read in the packets and store them in an array
        for i in range(count):
            arrival_time, process_time = map(int, input().strip().split())
            response=(self.Process(Request(arrival_time, process_time)))
            print(response.start_time if not response.dropped else -1)

            
def ProcessRequests(pp):
    # process the packets that are passed, use buffer to queue them
    responses = []      #holds response
    for request in pp.requests: #process each packet one at a time
        responses.append(pp.Process(request)) #append response into list of responses
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split()) #read input parameters: size: pp buffer size, count: number of packets to be processed


    pp=PackageProcessor(size, count)    #create a packet processor given a buffer with size "size" and incoming packet count of "count"

    

# python3
'''
    A simple phone book manager. One is able to add, delete and find name for
    a number.

    direct addessing scheme is used where the phone book array as indecese that
    are the phone numbers. This scheme utilizes a lot of memory

    example input
    12
    add 911 police
    add 76213 Mom
    add 17239 Bob
    find 76213
    find 910
    find 911
    del 910
    del 911
    find 911
    find 76213
    add 76213 daddy
    find 76213


    output
    Mom
    not found
    police
    not found
    Mom
    daddy
'''
class Query:
    def __init__(self, query):
        '''
        A Query is any of the following:
            add number name
            find number
            del number
        '''
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    '''

    '''
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    '''
    use direct accessing scheme
    
    '''
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [0 for _ in range(10000000)]     #big array is allocated for phone book
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number]=cur_query.name
        elif cur_query.type == 'del':
            contacts[cur_query.number]=0
        else:
            #Only find Query returns a response
            if contacts[cur_query.number] !=0:
                response = contacts[cur_query.number]
            else:
                response = 'not found'
            result.append(response)
    return result

'''
 using dictionary data structure to implement
def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number]=cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                contacts.pop(cur_query.number)
        else:
            if cur_query.number in contacts:
                response = contacts[cur_query.number]
            else:
                response = 'not found'
            result.append(response)
    return result
'''
if __name__ == '__main__':
    write_responses(process_queries(read_queries()))


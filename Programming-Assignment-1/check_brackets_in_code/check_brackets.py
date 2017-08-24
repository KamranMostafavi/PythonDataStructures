# python3

import sys
'''
    This is an example of use of a stack. Text is read and analysed
    for correct sequence of open/close brackets. A braket pair may be any of the
    following: ()[]{}. There may be other alphanumeral characters in the
    text. If a mismatch is encountered, then the position of mismatched open bracket
    is outputed, otherwise "success" is printed.

    file:///C:/Users/Kamran/Documents/eduction/data%20structures/Programming-Assignment-1/Programming-Assignment-1.pdf
'''


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        # returns true if character matches the closing of an open bracket
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":

    
    text = sys.stdin.read()

    opening_brackets_stack = []
    success=True
    for i, next in enumerate(text): #reads text as a character array returns character and its index in the array
        #print (i,next);
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            # push open barckets on to stack
            bracket=Bracket(next,i+1)
            opening_brackets_stack.append(bracket)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            # if stack is empty and a closed bracket is encountered then there
            # was a mismatch
            if len(opening_brackets_stack)==0:
                success=False
                bracket=Bracket(next,i+1)
                break;
            # pop the closed bracket off of the stack and check for a match
            bracket=opening_brackets_stack.pop()
            if not bracket.Match(next):
                success = False
                bracket.position=i+1    #position of the first open bracket that mismatched
                opening_brackets_stack.append(bracket)
                break

    # Printing answer, write your code here
    
    if (len(opening_brackets_stack)==1):
        #if a bracket left in the stack then it must be a mismatch
        success=False
        bracket=opening_brackets_stack.pop();
    
    if (success):
        print ('Success');
    else:
        print (bracket.position)
    
        
 

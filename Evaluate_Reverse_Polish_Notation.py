# Approach

'''
1.take the list of expression and convert it into a deque
2.Another deque is used as a stack
3.pop one element at a time from the deque and check if it is an operand or an operator.
4.if it is an operand push it on to the stack
5.if it is an operator pop two elements from the stack and evaluate them using the operator and push the answer back into the stack.
'''

# Code

import collections 

class Solution:
    def evalRPN(self, tokens) -> int:
        de = collections.deque(tokens)
        stack = collections.deque()
        
        while de:
            element = de.popleft()
            if element in ['+','-','/','*']:
                ex1 = stack.pop()
                ex2 = stack.pop()
                exp = str(ex2) + str(element) + str(ex1)
                ans = int(eval(exp))
                stack.append(ans)
            else:
                stack.append(element)
        
        return int(stack[0])
# Python program for implementation of stack
 
from sys import maxsize
 
def createStack():
    stk=[]
    return stk
 
def isEmpty(stk):
    return len(stk)== 0
    
def push(stk, item):
    stk.append(item)
    print(item + " pushed to stack ")
     
def pop(stk):
    if (isEmpty(stk)):
        return str(-maxsize -1) 
     
    return stk.pop()
 
def peek(stk):
    if (isEmpty(stk)):
        return str(-maxsize -1) 
    return stk[len(stk) - 1]
 
stk = createStack()
push(stk, str(10))
push(stk, str(20))
push(stk, str(30))
print(pop(stk) + " popped from stack")

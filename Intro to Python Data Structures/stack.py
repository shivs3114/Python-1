#This is code for LINEAR data structue STACK(LIFO) 



 
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
    
def Push(stk,item):
    stk=stk.append(item)
    top=len(stk)-1

def Pop(stk):
    if isEmpty(stk):
        return "UnderFlow":
    else:
        item=stk.pop()
        if isEmpty(stk):
            top=None
        else:
            top=len(stk)-1
    return item

def Peek(stk):
    if isEmpty(stk):
        return "UnderFlow"
    else:
        return stk[top]
    
def Display(stk):
    if isEmpty(stk):
        return "EMPTY STACK"
    else:
        for i in range(-(len(stk)-1),0,+1):
            print(stk(i))

def main():
    stk=list(input("enter stack:"))
    top=len(stk)-1
    Push(stk,2)
    Push(stk,15)
    Push(stk,3)
    Push(stk,5)
    Pop(stk)
    Peek(stk)
    Push(stk,67)
    Push(stk,89)
    Display(stk)

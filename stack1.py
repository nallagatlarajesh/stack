
def isEmpty(glassstack):
    if len(glassstack)==0:
        return True
    else:
        return False
def oppush(glassstack,element): #it is having two parameters stack name and element
    glassstack.append(element)  #append for insertion i.e built in function

def size(glassstack):
    return len(glassstack)
def top(glassstack):
    if isEmpty(glassstack):
        print("stack is empty")
        return None
    else:
        x=len(glassstack)
        element=glassstack[x-1]
        return element
def oppop(glassstack):
    if isEmpty(glassstack):
        print("underflow")
        return None
    else:
        return (glassstack.pop())
def display(glassstack):
    x=len(glassstack)
    print("current elements in the stack are:")
    for i in range(x-1,-1,-1):
        print(glassstack[i])
#object    
glasssstack=list()
#add elements to stack
element="glass1"
print("pushing element ",element)
oppush(glassstack,element)
element="glass2"
print("pushing element ",element)
oppush(glassstack,element)
#display number of elements in a stack
print("current number of elements in the stack",size(glassstack))

#delete an element from the stack
element=oppop(glassstack)
print("popped element",element)
#add new element to stack
element="glass3"
print("pusshing element is ",element)
oppush(glassstack,element)

#delete an element from tehstack
#the stack
element=oppop(glassstack)
print("popped element is ",element)
print("current elements in the stack is",size(glassstack))

    

'''
    STACKS
'''
''' A stack is a data structure that is often likened to a stack of plates. '''
class Node():
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Stack():
    
    def __init__(self):
        self.top = None
        self.size = 0
        
#     Push operation
# The push operation is used to add an element to the top of the stack.
        
    def push(self, data):
        node = Node(data)
        if self.top:
            node.data = self.top
            self.top = None
        else: self.top = node
        self.size += 1
        
#     Pop operation
# Now we need a pop method to remove the top element from the stack.
    def pop(self, data):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else: self.top = None
            return data
        else: return None
    
    # PEAK 
#     This will just return the top of the
# stack without removing it from the stack, allowing us to look at the top element without
# changing the stack itself
    def peek(self, data):
        if self.top:
            return self.top.data
        else: return None
        
    # Bracket-matching application
def check_brackets(statement):
    
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        if ch in ('}', ']', ')'):
            last = stack.pop()
        if last == '{' and ch != '}':
            continue
        elif last == '[' and ch != ']':
            continue
        elif last == '(' and ch != ')':
            continue
        else:
            return False
    if stack.size > 0:
        return False
    else:
        return True
    
sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)

for s in sl:
    m = check_brackets(s)
    print("{}: {}".format(s, m))
            

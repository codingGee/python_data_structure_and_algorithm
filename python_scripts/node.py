'''
    A node is a container of data, together with one or more links to other nodes. A link is a pointer.
'''

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
        def __str__(self):
            return str(data)
        
        
n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('span')
# print(n1)
# print(n2)
# print(n3)
# u

n1.next = n2
n2.next = n3
# print(n2)
# print(n3)

current = n1
while current:
    print(current.data)
    current = current.next 
    print(current)
'''
    Singly linked list class
'''

class SinglyLinkedList():
    def __init__(self):
        # start of the list 
        self.head = None
        # end of the list 
        self.tail = None
        # getting the size of the list 
        self.size = 0
        
# we can quickly append a new node at the end of the list. The
# worst case running time of the append operation is now reduced from O(n) to O(1). All we
# have to do is make sure the previous last node points to the new node, that is about to be
# appended to the list

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
            self.size += 1
            
#     Improving list traversal
# If you notice how we traverse our list. That one place where we are still exposed to the node
# class. We need to use node.data to get the contents of the node and node.next to get the
# next node.        
            
    def iter(self):
        current = self.tail 
        while current:
            val = current.data
            current = current.next
            yield val
            
# Another common operation that you would need to be able to do on a list is to delete nodes.
# This may seem simple, but we'd first have to decide how to select a node for deletion. 
    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail: 
                    self.tail = current.next
            else:
                prev.next = current.next
            self.size -= 1
            return
        prev = current
        current = current.next
        
#     List search
# We may also need a way to check whether a list contains an item. This method is fairly easy
# to implement thanks to the iter() method we previously wrote. Each pass of the loop
# compares the current data to the data being searched for. If a match is found, True is
# returned, or else False is returned:
    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False
    
# Clearing a list
# We may want a quick way to clear a list. Fortunately for us, this is very simple. All we do is
# clear the pointers head and tail by setting them to None :
    def clear(self):
        # clear the entire list 
        self.head = None
        self.tail = None
        
        
        
        
''' We can append a few items: '''
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('span')


''' List traversal will work more or less like before. You will get the first element of the list
from the list itself: '''
current = words.tail
while current:
    print(current.data)
    current = current.next
    
    
    ''' Improving list traversal '''
''' But we mentioned earlier that client code should never need to interact with
Node objects. '''


counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 1000:
        break
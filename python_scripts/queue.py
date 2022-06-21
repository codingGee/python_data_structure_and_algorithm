'''
    Queues
Another special type of list is the queue data structure. This data structure is no different
from the regular queue you are accustomed to in real life
'''

class ListQueue():
    
    def __init__(self):
        self.items = []
        self.size = 0
    '''
        Enqueue operation
    The enqueue operation or method uses the insert method of the list class to insert items
    (or data) at the front of the list:
    '''
    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1
        
    #     Dequeue operation
    # The dequeue operation is used to remove items from the queue.
    def dequeue(self, data):
        data = self.items.pop()
        self.size -= 1
        return data
    '''    
    Stack-based queue
    Yet another implementation of a queue is to use two stacks. Once more, the Python list
    class will be used to simulate a stack
    '''
    class Queue():
        def __init__(self):
            self.inbound_stack = []
            self.outbound_stack = []
            
        def enqueue(self, data):
            self.inbound_stack.append(data)
            
            # to remover element from our queue 
            if not self.outbound_stack:
                while self.inbound_stack:
                    self.outbound_stack.append(self.inbound_stack.pop())
            return self.outbound_stack.pop()
                    
        
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.inbound_stack)
    
    # print(queue.inbound_stack)
    # print(queue.outbound_stack)
    # print(queue.outbound_stack)

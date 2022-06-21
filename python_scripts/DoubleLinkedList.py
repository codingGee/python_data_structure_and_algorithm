'''  Doubly linked lists '''
'''
A doubly linked list is somehow similar to a singly linked list in that we make use of the
same fundamental idea of stringing nodes together. In a Singly linked list, there exists one
link between each successive node. A node in a doubly linked list has two pointers: a
pointer to the next node and a pointer to the previous node:
'''

''' In a doubly linked list, we add to each node the ability to not only reference the next node
but also the previous node. '''

''' A Doubly lined list node '''

class Node(object):
    
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
        
    
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    # adding a new node to the list 
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            # The else part of the algorithm is only executed if the list is not empty. The new node's
            # previous variable is set to the tail of the list:
            new_node.prev = self.tail
            # The tail's next pointer (or variable) is set to the new node:
            self.tail.next = new_node
            # Lastly, we update the tail pointer to point to the new node:
            self.tail = new_node
            # Since an append operation increases the number of nodes by one, we increase the counter by one:
            self.count += 1  
            
            
    # Delete operation
    def delete(self, data):
        current = self.head
        node_deleted = False
# The head node is searched first. Since current is pointing at head , if current is None, it is
# presumed that the list has no nodes for a search to even begin to find the node to be
# removed:
        if current is None:
            node_deleted = False
# However, if current (which now points to head) contains the very data being searched for,
# then self.head is set to point to the current next node. Since there is no node behind
# head now, self.head.prev is set to None
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
# A similar strategy is adopted if the node to be removed is located at the tail end of the list.
# This is the third statement that searches for the possibility that the node to be removed
# might be located at the end of the list:
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
# Lastly, the algorithm to find and remove a node loops through the list of nodes. If a
# matching node is found, current 's previous node is connected to current's next node.
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current.next
                if node_deleted:
                    self.count += 1
# To delete node B in the middle of the list, we will essentially make A
# point to C as its next node, while making C point to A as its previous node:

# List search
# The search algorithm is similar to that of the search method in a singly linked list. We call
# the internal method iter() to return the data in all the nodes. As we loop through the
# data, each is matched against the data passed into the contain method. If there is a match,
# we return True , or else we return False to symbolize that no match was found:
    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
            return False
        
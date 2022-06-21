'''Priority queues and heaps'''
"""A heap is a data structure that satisfies the heap property. The heap property states that
there must be a certain relationship between a parent node and its child nodes. This
property must apply through the entire heap."""

class Heap():
    
    def __init__(self):
        self.heap = [0]
        self.size = 0
        
    def float(self, k):
        # Since we are using integer division, as soon as we get
        # below 2, the loop will break out:
        while k // 2 > 0:
        # Compare parent and child. If the parent is greater than the child, swap the two values:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap
            # Finally, let's not forget to move up the tree: 
            k // 2
            # This method ensures that the elements are ordered properly. Now we just need to call this
            # from our insert method:
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.float(self.size)
    
    # Just like insert, pop() is by itself a simple operation. We remove the root node and
    # decrement the size of the heap by one.
    def minindex(self, k):
        if k * 2 <= self.size:
            return k * 2
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2
        else:
            return k * 2 + 1
        
    # Now we can create the sink function:
    def sink(self, k):
        while k * 2 <= self.size:
            mi = self.minindex(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi]
                self.heap[k]
                k = mi
            
    def pop(self, k):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item
    
    def heap_sort(self):
        sorted_list = []
        for node in range(self.size):
            n = self.pop()
            sorted_list.append(n)
        return sorted_list
    
    
h = Heap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
print(h.heap)

for i in range(10):
    n = h.pop()
    print(n)
    print(h.heap)
''' Breadth-first traversal '''
from collections import deque
   
   
   
class Tree():
    def breath_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            
            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)
        return list_of_nodes
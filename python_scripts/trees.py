
''' how to build a binary tree node class in Python: '''

class Node():
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    # Binary search tree implementation

class Tree():
    
    def __init__(self):
        self.root_node = None
    # The method that returns the minimum node is as follows:
    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current
    
    # Let's now create a function that enables us to add data as nodes to the BST
    def insert(self, data):
        node = Node(data)
        # A first check will be to find out whether we have a root node. If we don't, the new node
        # becomes the root node (we cannot have a tree without a root node):     
        if self.root_node is None:
            self.root_node = node
        else:
            # As we walk down the tree, we need to keep track of the current node we are working on
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return
                    
    # Our node class does not have reference to a parent. As such, we need to use a helper
    # method to search for and return the node with its parent node.  
    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child 
                return (parent, current)
    
    
    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        
        if parent is None and node is None:
            return False
        
        # get children count 
        children_count = 0
        
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1 
        
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
            # In the case where the node about to be deleted has only one child, the elif part
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child 
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
                
            # Lastly, we handle the condition where the node we want to delete has two children:
        else:
            parent_of_leftmost_node = None
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child
                
    def search(self, data):
        current = self.root_node
        while True:
            # if there's no node 
            if current is None:
                return None
            # if there's a node with data 
            elif current.data is data:
                return data
            # using the BST of arranging nodes from the rootnode 
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
                
# tree = Tree()
# tree.insert(5)
# tree.insert(2)
# tree.insert(7)
# tree.insert(9)
# tree.insert(1)

# for i in range(1, 10):
#     found = tree.search(i)
#     print("{}: {}".format(i, found))
        
    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)
    
    def postorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.postorder(current.left_child)
        self.postorder(current.right_child)
        
        print(current.data)
        

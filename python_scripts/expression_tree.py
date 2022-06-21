'''
    Expression trees
    The tree structure is also used to parse arithmetic and Boolean expressions. For example,
    the expression tree for 3 + 4 would look as follows:
'''

class Stack():
    
    def __init__(self):
        self.pop = None
        self.push = None
        
        
class TreeNode():
    
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
    
    
expr = "4 5 + 5 3 - *".split()
stack = Stack()

for term in expr:
    if term in "+-/":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
    stack.push(node)
    
def calc(node):
    if node.data is "+":
        return calc(node.left)
    elif node.data is "-":
        return calc(node.left)
    elif node.data is "*":
        return calc(node.left)
    elif node.data is "/":
        return calc(node.left)
    else:
        return node.data
root = stack.pop()
result = calc(root)
print(result)
    
        
        

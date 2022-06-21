
''' using special methods like the builtin methods'''

class my_class():
    def __init__(self, greet) -> None:
        self.greet = greet
        
    def __repr__(self) -> str:
        return f"custom object ('{self.greet}')"
    
# create an instance the class 
''' an instance is a variable assigned a class
        or a class assigned to a variable
'''
a = my_class('codingGee')
print(a)
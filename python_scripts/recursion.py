''' 
    In Python, we can implement a recursive function simply by calling it within its own function body
'''

def iterTest(low, high):
    while low <= high:
        print(f'low interTest val: {low}')
        low=low+1
        
print(iterTest(2, 5))    
''' iteration test '''

def recurTest(low, high):
    if low <= high:
        print(f'low recurTest val: {low}')
        recurTest(low+1, high)
        
print(recurTest(3, 9))
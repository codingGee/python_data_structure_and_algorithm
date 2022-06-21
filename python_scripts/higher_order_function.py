''' Functions that take other functions as arguments, 
or that return functions, are called higher order functions. '''

''' Map function'''

lst = [1,2,3,4]

print(list(map(lambda x: x**3, lst)))

''' filter function '''
print(list(filter(lambda x: x < 3, lst)))
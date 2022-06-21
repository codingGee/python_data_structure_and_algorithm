'''
    The array module defines a datatype array that is similar to the list datatype except for
    the constraint that their contents must be of a single type of the underlying representation,
    as is determined by the machine architecture or underlying C implementation
'''


# It should be noted that when performing operations on arrays that create lists, such as list
# comprehensions, the memory efficiency gains of using an array in the first place will be
# negated. When we need to create a new data object, a solution is to use a generator
# # expression to perform the operation, for example:

import array
ba = array.array('i', range(10**6))
bl = list(range(10**6))


import sys
print(100 * sys.getsizeof(ba) / sys.getsizeof(bl))
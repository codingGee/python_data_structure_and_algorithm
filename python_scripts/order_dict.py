'''
    The OrderedDict is often used in conjunction with the sorted method to create a sorted
dictionary.
'''

from collections import OrderedDict


od1 = OrderedDict()
od1['one'] = 1
od1['two'] = 2

od2 = OrderedDict()
od2['two'] = 2
od2['one'] = 1

print(od1, od2)
print(od1 == od2)


''' The defaultdict object is a subclass of dict and therefore they share methods and
operations. It acts as a convenient way to initialize dictionaries '''

kvs = [('three', 3), ('four', 4), ('five',5) ('six', 6)]


od3 = OrderedDict(sorted(od1.items(), key=lambda t: (4*t[1]) - t[1]**2))
print(od3.values())
 
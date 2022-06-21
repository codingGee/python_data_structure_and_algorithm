''' Chain Maps
it provides a way to link a
number of dictionaries, or other mappings, so that they can be treated as one object. In
addition, there is a maps attribute, a new_child() method, and a parents property. The
underlying mappings for ChainMap objects are stored in a list and are accessible using the
maps[i] attribute to retrieve the ith dictionary. Note that even though dictionaries
themselves are unordered, ChainMaps are an ordered list of dictionaries. ChainMap is
useful in applications where we are using a number of dictionaries containing related data.
The consuming application expects data in terms of a priority, where the same key in two
dictionaries is given priority if it occurs at the beginning of the underlying list. ChainMap is
typically used to simulate nested contexts such as when we have multiple overriding
configuration settings. The following example demonstrates a possible use case for

'''

from collections import ChainMap
from collections import Counter

defaults = {'theme':'Default', 'language':'English', 'showIndex':True, 'showFooter':True}

print('# create chainMap with a default configuration')
cm=ChainMap(defaults)
print('# Print configurations..')
print(cm)


print('# create a new child that overrides the parent')
cm2=cm.new_child({'theme':'bluesky'})
print(cm2)

print(''' in removing the new theme. the first theme appears which is the default''')
print(cm2.pop('theme'))
print(cm2)

# add a new content as a new_child 
cm2.maps[0] = {'theme':'desert', 'showIndex':False}
print(cm2)
print(cm2['showIndex'])
print(cm2.parents)


# using counter 
ct = Counter()
print('# populate the counter') 
ct.update('abca')
print(ct)
print(
    'updating the counter properities'
)
ct.update({'a':3})
print(ct)
# loop throught counter object 
for item in ct:
    print(item, ct[item])

print(
    'the counter elements'
)
print(sorted(ct.elements()))

print(
    'get the most common value'
)
print(
    'substract from the c1 val '
)
ct.subtract({'a':2})
print(ct)
print(
    ' we subtracted the value of 2 from "a":5 '
)
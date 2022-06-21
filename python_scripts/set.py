''''


Sets are unordered collections of unique items. Sets are themselves mutable, we can add
and remove items from them; however, the items themselves must be immutable. An
important distinction with sets is that they cannot contain duplicate items. Sets are typically
used to perform mathematical operations such as intersection, union, difference, and
complement.

'''

s1 = {
    'ab', 3,4,(5,6)
}

s2 = {
    'ab', 7,(7,6)
}

''' Difference returns a set of all items in s1 and not in s2 '''
# get the difference
print(s1-s2)

''' Intersection returns a set of all items in both s1 and s2 '''
# intersection,
print(s1.intersection(s2))
''' Intersection returns True if all items in s1 are also in s2 '''
# union
print(s1.union(s2))



''' The frozenset , on the other hand, is immutable and therefore able
to be used as a member of a set: '''

fs1 = frozenset(s1)
fs2 = frozenset(s2)
print({
    fs1: 'fs1',
    fs2: 'fs2' 
})
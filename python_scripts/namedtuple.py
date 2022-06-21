'''
    The namedtuple method returns a tuple-like object that has fields accessible with named
indexes as well as the integer indexes of normal tuples.
'''

from collections import defaultdict
from difflib import IS_CHARACTER_JUNK




dd = defaultdict(int)
words = str.split('red blue green yellow blue red green green red')
for word in words: dd[word] +=1
print(dd)



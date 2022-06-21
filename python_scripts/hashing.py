''' Hashing is the concept of converting data of arbitrary size into data of fixed size. '''
print(ord('f'))  #getting the hashing of f string

''' To get the hash of the whole string, we could just sum the
ordinal numbers of each character in the string: '''
print(sum(map(ord, 'hello world')))


# Perfect hashing functions
'''we live with the fact that we sometimes get collisions (two
or more strings having the same hash value), and when that happens, we come up with a
strategy for resolving them'''

'''could, for example, add a multiplier, so that the hash value for each character becomes the
multiplier value, multiplied by the ordinal value of the character. The multiplier then
increases as we progress through the string.'''

def myHash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult * ord(ch)
        mult += 1
    return hv

for item in ('ad','ga'):
    print(f'{item}: {myHash(item)}')
    
'''
    Hash table
A hash table is a form of list where elements are accessed by a keyword rather than an
index number. At least, this is how the client code will see it.
'''

class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        

class HashTable():
    
    # creating a class to hold hash table items
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        
    # hash table
    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size
    
    # Putting elements
    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        
        # checking the slot for val 
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item 
        
        # Getting elements
    def get(self, key):
        h = self._hash(key)
        # list for an element that has the key
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size
        return None
    
    # Using [] with the hash table
    def __setitem__(self, key, value):
        self.put(key, value)
        
    def __getitem__(self, key):
        return self.get(key)
    
ht = HashTable()
ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"

for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get(key)
    print(v)
print(f'The number of element is: {ht.count}')
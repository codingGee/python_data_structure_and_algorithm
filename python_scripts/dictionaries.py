''' Dictionaries are arbitrary collections of objects indexed
    by numbers, strings, or other immutable objects
'''
# Dictionaries themselves are mutable; however, their index keys must be immutable.


dict = {
    'one':1,
    'two':2,
    'three':3
}


dict.update(
    {'four': 4,
    'five':5,
     'six':6}
)
        


# we use the __getitem__ special method to sort the dictionary keys according to the
# dictionary values:

# print(sorted(list((dict))))
# arrange a dict 
# print(sorted(list(dict), key=dict.__getitem__ , reverse= True))
# print the val in a dict
# print([value for (key, value) in sorted(dict.items())])

'''  
    Now, let's say we are given the following dictionary, English words as keys and French
    words as values. Our task is to place these string values in correct numerical order:
'''

d2 ={
    'one':'uno' ,
    'two':'deux',
    'three':'trois',
    'four': 'quatre',
    'five':'cinq',
    'six':'six'
    }

print(sorted(d2, key=dict.__getitem__))

''' Since our keys in both dictionaries are the same, we can use a list
    comprehension to sort the values of the French to English dictionary:
'''
print([d2[i] for i in sorted(d2, key=dict.__getitem__)])

''' a typical example is counting the occurrences of words in a body of text. The following code
    creates a dictionary where each word in the text is used as a key and the number of
    occurrences as its value
'''

def wordcount(fname):
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened')
        exit()
        
    count = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return(count) 

count = wordcount('alice.txt')
filtered = { key:value for key, value in count.items() if value < 20 and value > 15}
# Generators

# compare the running time of a list compared to a generator 
import time


''' Generator function creates an iterator of odd numbers betweeb n and m '''

def oddGen(n, m):
    while n < m:
        # ''' What Is Yield In Python? The Yield keyword in Python
        # is similar to a return statement used for returning values 
        # or objects in Python. However, there is a slight difference. 
        # The yield statement returns a generator object to the one who
        # calls the function which contains yield, 
        # instead of simply returning a value. '''
        
        yield n
        n += 2
        #Generators never return a value other than None .
        
        

''' Build a list of odd numbers between n and m '''
def oddList(n, m):
    # create a list
    list = []
    # pass a condition btw the function argument n and m
    while n < m:
        # if n is less than m, add n ot the list
        list.append(n)
        # add the value of n
        n +=2
        # return the list 
    return list


''' The time it takes to perform such iteration '''
t1=time.time()
sum(oddGen(1,1000000))
print("Time to sum an iterator: %f" % (time.time() - t1))
''' the time it takes to build and sum a list '''
t1=time.time()
sum(oddList(1,1000000))
print("Time to build and sum a list: %f" % (time.time() - t1))

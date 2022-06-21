'''
    The recursive factorial algorithm defines two cases: the base case when n is zero,
and the recursive case when n is greater than zero. A typical implementation is the following:
'''

def factorial(n):
    # test for a base case 
    if n == 0:
        return 1
    # make a calculation and a recursive call 
    f = n*factorial(n-1)
    print(f)
    return(f)
# print(factorial(4))

'''
    Backtracking
Backtracking is a form of recursion that is particularly useful for types of problems such as
traversing tree structures, where we are presented with a number of options at each node,
from which we must choose one
'''

def bitStr(n, s):
    if n == 1: return s
    return [ digit + bits for digit in bitStr(1, s) for bits in bitStr(n-1,s)]
print(bitStr(3, 'abc'))

'''
    The Karatsuba algorithm
improves on this is by making the following observation. We really only need to know three
quantities: z 2 = ac ; z 1 =ad +bc, and z 0 = bd to solve equation

his shows that we can indeed compute the sum of ad + bc without separately computing
each of the individual quantities. In summary, we can improve on equation 3.1 by reducing
from four recursive steps to three. These three steps are as follows:
1. Recursively calculate ac.
2. Recursively calculate bd.
3. Recursively calculate (a +b)(c + d) and subtract ac and bd.
The following example shows a Python implementation of the Karatsuba algorithm:

'''


from math import log10
import math
import random


def karatsuba(x, y):
    #the nase case for recursion 
    if x < 10 or y < 10:
        return x * y
    # sets n, the number of digits in the highest input number 
    n = max(int(log10(x) + 1), int(log10(y)+1))
    # rounds up n/2 
    n_2 = int(math.ceil(n/2.0))
    # add 1 if n is uneven
    n = n if n % 2 == 0 else n + 1
    # splits the input numbers 
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)
    # applies the three recursive steps 
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac - bd
    # perform the multiplication 
    return (((10**n)*ac) + bd + ((10**n_2) * (ad_bc))) 

''' To satisfy ourselves that this does indeed work, we can run the following test function: '''

def test():
    for i in range(1000):
        x = random.randint(1, 10**5)
        y = random.randint(1, 10**5)
        expected = x * y
        result = karatsuba(x, y)
        if result != expected:
            return('failed!')
        return('Passed!!')
print(test())

''' Here is the Python code for the merge sort algorithm: '''

def mergeSort(A):
    #base case if the input array is one or zero just return.
    if len(A) > 1:
    # splitting input array
        print('splitting ', A )
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
    #recursive calls to mergeSort for left and right sub arrays
        mergeSort(left)
        mergeSort(right)
    #initalizes pointers for left (i) right (j) and output array(k)
    # 3 initalization operations
        i = j = k = 0
    #Traverse and merges the sorted arrays
        while i <len(left) and j<len(right):
    # if left < right comparison operation
            if left[i] < right[j]:
    # if left < right Assignment operation
                A[k]=left[i]
                i=i+1
            else:
    #if right <= left assignment
                A[k]= right[j]
                j=j+1
                k=k+1
        while i<len(left):
    #Assignment operation
            A[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
    #Assignment operation
            A[k]=right[j]
            j=j+1
            k=k+1
            print('merging ', A)
            return(A)
        
        
# run the program 
mergeSort([356, 97, 846, 215])
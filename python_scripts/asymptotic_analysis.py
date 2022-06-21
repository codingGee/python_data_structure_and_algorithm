'''
    Asymptotic analysis
    There are essentially three things that characterize an algorithm's runtime performance.
    They are:
    Worst case - Use an input that gives the slowest performance
    Best case - Use an input that give, the best results
    Average case - Assumes the input is random
    To calculate each of these, we need to know the upper and lower bounds. We have seen a
    way to represent an algorithm's runtime using mathematical expressions, essentially adding
    and multiplying operations. To use asymptotic analyses, we simply create two expressions,
    one each for the best and worst cases.
'''

'''
    We can see that
    inserting an item occurs in O(n) time and sorting is O(nlogn) time. We can write the total
    time complexity as O(n + nlogn), that is, we bring the two functions inside the O(...).
'''

''' c0 +c1 n + cn = O(n ). '''

n = 500 #c0

# excute the n times 
for i in range(0, n):
    print(i)  #c1
# excute the n times 
for i in range(0, n):
    # excute the n times 
    for j in range(0, n):
        print(j)
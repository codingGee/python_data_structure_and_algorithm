# The Memoization technique
# Let's generate the Fibonacci series to the fifth term:


def fib(n):
    if n <= 2:
        return 1
    else: return fib(n-1) + fib(n-2)
    
def dyna_fib(n, lookup):
    if n <= 2:
        lookup[n] = 1
    if lookup[n] is None:
        lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup)
    return lookup[n]


'''The tabulation technique
There is a second technique in dynamic programming, which involves the use of a table of
results or matrix in some cases to store results of computations for later use.'''

def fib(n):
    results = [1, 1]
    for i in range(2, n):
        results.append(results[i-1] + results[i-2])
    return results[-1]


'''Merge Sort'''
def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    
    mid_point = int((len(unsorted_list)) //2 )
    first_half = unsorted_list[:mid_point]
    last_half = unsorted_list[mid_point:]
    half_a = merge_sort(first_half)
    half_b = merge_sort(last_half)
    
    return merge(half_a, half_b)


# merge function 
def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else: 
            merged_list.append(second_sublist[j])
            j += 1
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list

list = [4,5,8,9,1,2,3,4,10,11,12,13]

print(merge_sort(list))
        
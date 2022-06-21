'''Bubble sort
The idea behind a bubble sort algorithm is very simple. Given an unordered list, we
compare adjacent elements in the list, each time, putting in the right order of magnitude, only two elements'''

def bubble_sort(unordered_list):
    iteration_number = len(unordered_list) - 1
    for j in range(iteration_number):
        for j in range(iteration_number):
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp


''' SELECTION SORT '''
def selected_sort(unsorted_list):
    size_of_list = len(unsorted_list)
    for i in range(size_of_list):
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[i]:
                print(unsorted_list[i])
                print(unsorted_list[j])
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
                
'''Quick sort
The quick sort algorithm falls under the divide and conquer class of algorithms, where we
break (divide) a problem into smaller chunks that are much simpler to solve (conquer). In
this case, an unsorted array is broken into sub-arrays that are partially sorted, until all
elements in the list are in the right position, by which time our unsorted list will have
become sorted.'''

''' first we define the partition function '''

def partition(unsorted_array, first_index, last_index):
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1
    
    while True:
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            less_than_pivot_index -= 1
            
        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else: 
            break
        unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
        unsorted_array[less_than_pivot_index] = pivot
        return less_than_pivot_index
    
'''def the quick sort function '''
def quick_sort(unsorted_array, first, last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_array, first, last)
        quick_sort(unsorted_array, first, partition_point - 1)
        quick_sort(unsorted_array, partition_point + 1)
        
'''HEAP SORT '''
from python_scripts.heaps import Heap


h = Heap()
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
for i in unsorted_list:
    h.insert(i)
    print("Unsorted list: {}".format(unsorted_list))
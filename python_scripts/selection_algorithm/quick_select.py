''' The quick select algorithm is used to obtain the ith-smallest element in an unordered list of
items, in this case, numbers '''


def quick_select(array_list, left, right, k):
    split = partition(array_list, left, right)
    if split == k:
        return array_list[split]
    elif split < k:
        return quick_select(array_list, split + 1, right, k)
    else: return quick_select(array_list, left, split - 1, k)
    
    # partition step 
def partition(unsorted_array, first_index, last_index):
    if first_index == last_index:
        return first_index
    else:
        nearest_median = median_of_medians(unsorted_array[first_index:last_index])
    
    index_of_nearest_median = get_index_of_nearest_median(unsorted_array, first_index, last_index, nearest_median)
    swap(unsorted_array, first_index, index_of_nearest_median)    
    
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1
    
    while True:
        
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
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
    
def median_of_medians(elems):
    sublists = [elems[j:j+5] for j in range(0, len(elems), 5)]
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist)/2])
    if len(medians) <= 5:
        return sorted(medians)[len(medians)/2]
    else: return median_of_medians(medians)
    
def get_index_of_nearest_median(array_list, first, second, median):
    if first == second:
        return first
    else: return first + array_list[first:second].index(median)
    
def swap(array_list, first, second):
    temp = array_list[first]
    array_list[first] = array_list[second]
    array_list[second] = temp
    
def deterministic_select(array_list, left, right, k):
    split = partition(array_list, left, right)
    if split == k:
        return array_list[split]
    elif split < k:
        return deterministic_select(array_list, split + 1, right, k)
    else: return deterministic_select(array_list, split -1, left, k)
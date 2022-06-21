'''Searching algorithms are categorized under two broad types. One category assumes that
the list of items to apply the searching operation on, has already been sorted whiles the
other does not.
'''

'''Linear Search'''

# Unordered linear search


def search(unordered_list, term):
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        if term == unordered_list[i]:            
            return i
    return None


''' Ordered Linear Search '''
def ordered_search(ordered_list, term):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return None
    return None

'''BINARY SEARCH  '''
'''A binary search is a search strategy used to find elements within a list by consistently
reducing the amount of'''

def binary_search(ordered_list, term):
    size_of_list = len(ordered_list)
    
    # get accurate index 
    index_of_first_element = 0
    index_of_last_element = size_of_list
    
    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)//2
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else: index_of_last_element = mid_point - 1
    if index_of_first_element > index_of_last_element:
        return None
    
def binarySearch(ordered_list, first_index_element, last_index_element, term):
    if (last_index_element < first_index_element):
        return None
    else: mid_point = first_index_element + ((last_index_element - first_index_element)//2)
    if ordered_list[mid_point] > term:
        return binarySearch(ordered_list, first_index_element, mid_point - 1, term)
    elif ordered_list[mid_point] < term:
        return binarySearch(ordered_list, mid_point + 1, last_index_element, term)
    else: return mid_point
    
'''A call to this recursive implementation of the binary search algorithm and its output is as
follows:'''
store = [2, 4, 5, 12, 43, 54, 60, 77]
print(binarySearch(store, 0, 7,2))


''' Interpolations Search '''
def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index + ((upper_bound_index - lower_bound_index) 
                                // (input_list[upper_bound_index] - input_list[lower_bound_index])) * (search_value - input_list[lower_bound_index])
    
# search_list = [44, 60, 75, 100, 120, 230, 250]
# lower_bound_index = 0
# upper_bound_index = 6
# input_list[upper_bound_index] = 250
# input_list[lower_bound_index] = 44
# search_value = 230

''' Interpolation search
There is another variant of the binary search algorithm that may closely be said to mimic
more, how humans perform search on any list of items. It is still based off trying to make a
good guess of where in a sorted list of items, a search item is likely to be found.'''

def interpolation_search(ordered_list, term):
    size_to_list = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = size_to_list
    
    while index_of_first_element <= index_of_last_element:
        mid_point = nearest_mid(ordered_list, index_of_first_element, index_of_last_element, term)
        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return True
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else: index_of_last_element = mid_point = 1
    if index_of_first_element > index_of_last_element:
        return None
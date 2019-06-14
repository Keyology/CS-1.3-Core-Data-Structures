#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if(len(array) > index):
        # print("INDEX", array[index])
        if(array[index] == item):
            return array[index]
        else:
            index += 1
            return linear_search_recursive(array, item, index)
    else:
        return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    """
        Iterative Binary search function -> O(logn) runtime
    """
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if item == val:
            return x
        elif item > val:
            if lower == x:
                break
            lower = x
        elif item < val:
            upper = x


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
     # Base case for exiting recusive function
    """
        Recursive Binary search function -> O(logn) runtime
    """

    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if left > right:
        return

    mid = (left + right) // 2
    print("LEFT 1", left)
    print("RIGHT 1", right)
    print("MID", mid)

    if array[mid] > item:
        right = mid - 1
        return binary_search_recursive(array, item, left, right)

    if array[mid] < item:
        left = mid + 1
        return binary_search_recursive(array, item, left,  right)
    print("*****MID*****", mid)

    return mid


list_of_nums = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick']
item = "Alex"
print(binary_search_recursive(list_of_nums, item))
# print(binary_search_iterative(list_of_nums, item))

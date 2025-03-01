"""
Problem statement #
An array of boolean values is divided into two sections: the left section consists of all false, and the right section consists of all true. Find the boundary of the right section, i.e. the index of the first true element. If there is no true element, return -1.

Example #
Input: arr = [false, false, true, true, true]

Output: 2

Explanation: first true's index is 2.

"""



from typing import List

def find_boundary(arr: List) -> int:
    # given array of bool
    # starti9ng with false
    # having true in middle or no true at all
    # find the find_boundary
    # we can perfcorm binary search to find the position of true
    # but since there are multiple true, we need the leftmost true
    # if we encounter a true, we move to left if adjacent element is true 
    # terminating condition is if left adjacent to mid is false , mid is true 
    mid = 0
    low = 0
    high = len(arr) - 1
    index_true = -1


    while low <= high:
        # when low == high last element is possible
        mid = (low + high) // 2

        if arr[mid] == True:
            # check left
            if (mid - 1 >= 0 and arr[mid - 1] == False) or mid  == 0:
                # found
                index_true = mid
                break
                # Immediate Termination
            else:
                # move left 
                high = mid - 1
                # if high < low it should terminate
        else:
            # if false go right
            low = mid + 1
    return index_true
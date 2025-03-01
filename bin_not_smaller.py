"""
NOT SMALLER

Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger or equal to the target. Assume that it is guaranteed to find a satisfying number.

Example #
Input: arr = [1, 3, 3, 5, 8, 8, 10],target = 2

Output: 1

Explanation: the first element larger than 2 is 3, which has index 1.


"""



from typing import List

def find_first_larger_or_equal(arr: List, target: int) -> int:

    mid = 0
    low = 0
    high = len(arr) - 1
    index = -1


    while low <= high:
        # when low == high last element is possible
        mid = (low + high) // 2
        # print(arr[mid])
        if arr[mid] >= target:
            # check left
            if (mid - 1 >= 0 and arr[mid - 1] < target) or mid  == 0:
                # found
                index = mid
                break
                # Immediate Termination
            else:
                # solution in left side
                high = mid - 1
                # if high < low it should terminate
        else:
            # soln in right
            low = mid + 1
    return index
             

arr = [1, 3, 3, 5, 8, 8, 10]
target = 2
print("res = ", find_first_larger_or_equal(arr, target))

print("res = ", find_first_larger_or_equal([0], 0))

print("res = ", find_first_larger_or_equal([1,2,3,4,5,6,7,8,9,10], 10))

print("res = ", find_first_larger_or_equal([1,1,1,1,4,5], 3))

"""
Problem statement #
Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

Example #
Input:arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100],target = 3

Output:1

Explanation: The first occurrence of 3 is at index 1.
"""


from typing import List

def find_first_occurrence(arr: List, target: int) -> int:

    mid = 0
    low = 0
    high = len(arr) - 1
    index = -1


    while low <= high:
        # when low == high last element is possible
        mid = (low + high) // 2
        # print(arr[mid])
        if arr[mid] == target:
            # check left
            if (mid - 1 >= 0 and arr[mid - 1] != target) or mid  == 0:
                # found
                index = mid
                break
                # Immediate Termination
                # avoid further loops
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
print("res = ", find_first_occurrence(arr, target))

print("res = ", find_first_occurrence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3))

print("res = ", find_first_occurrence([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))

print("res = ", find_first_occurrence([1, 22, 22, 33, 50, 100, 20000], 33))
print("res = ", find_first_occurrence([4, 6, 7, 7, 7, 20], 8))
print("res = ", find_first_occurrence([6, 7, 9, 10, 10, 10, 90], 10))

print("res = ", find_first_occurrence([4], 4))

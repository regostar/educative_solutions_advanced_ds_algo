"""
Problem statement #
A mountain array is defined as an array that:

Has at least 3 elements.
Has an element with the largest value called the “peak”, at an index k. The array elements monotonically increase from the first element to A[k], and then monotonically decreases from A[k + 1] to the last element of the array. Thus creating a “mountain” of numbers.
Find the index of the peak element. Assume there are no duplicates.

Example #
Input: 0 1 2 3 2 1 0

Output: 3

Explanation: The largest element is 3 and its index is 3.

"""


from typing import List

def rotated_sorted_arr(arr: List) -> int:
    # no peak duplicates
    #  0 1 2 3 2 1 0
    # compare arr[i] and arr[i+1]
    # arr[i] > arr[i+1]
    # F F F T T T T 
    # prob reduced to fidning the first True element
    mid = 0
    low = 0
    high = len(arr) - 1
    index = -1


    while low <= high:
        # when low == high last element is possible
        mid = (low + high) // 2
        # print(arr[mid])
        if mid + 1 < len(arr) and arr[mid] > arr[mid+1]:
            # check left
            # found
            index = mid
            high = mid - 1
        else:
            # soln in left
            low = mid + 1
            
            
    return index
             

arr = [1, 3, 3, 5, 8, 8, 10]
target = 2
print("res = ", rotated_sorted_arr(arr))

print("res = ", rotated_sorted_arr([30,40,50,40,30]))

print("res = ", rotated_sorted_arr([0,1,2,3,2,1,0]))

print("res = ", rotated_sorted_arr([0, 10, 0]))


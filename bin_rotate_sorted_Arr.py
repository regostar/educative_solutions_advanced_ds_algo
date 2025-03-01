"""
Problem statement #
A sorted array was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. Find the index of the minimum element in this array.

Example #
Input: [30, 40, 50, 10, 20]

Output: 3

Explanation: The smallest element is 10 and its index is 3.
"""



from typing import List

def rotated_sorted_arr(arr: List) -> int:

    mid = 0
    low = 0
    high = len(arr) - 1
    index = -1


    while low <= high:
        # when low == high last element is possible
        mid = (low + high) // 2
        # print(arr[mid])
        if arr[mid] <= arr[-1]:
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

print("res = ", rotated_sorted_arr([30,40,50,10,20]))

print("res = ", rotated_sorted_arr([0,1,2,3,4,5]))

print("res = ", rotated_sorted_arr([0]))


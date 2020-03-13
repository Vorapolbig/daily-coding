"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.
"""

arr = [1,0,2,3,0,4,5,0]
def solution(arr):
    n = len(arr)
    i = 0
    while i < n-1:
        if arr[i] == 0:
            arr.insert(i+1,0)
            arr.pop()
            i += 2
        else: 
            i += 1
    return arr
print(solution(arr))



"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.
"""

def solution(arr):
    output = []
    for i in range(1,len(arr)):
        output.append(max(arr[i:]))
    output.append(-1)
    return output

arr = [17,18,5,4,6,1]
print(solution(arr))
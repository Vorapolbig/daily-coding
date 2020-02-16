"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, 
also in sorted non-decreasing order.
"""
import numpy as np
def solution(A):
    arr = np.array(A)
    return sorted(arr*arr)

A = [-4,-1,0,3,10]
print(solution(A))
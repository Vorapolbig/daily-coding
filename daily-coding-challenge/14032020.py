"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.
"""

import math
from itertools import combinations

def heron_area(a,b,c):
    s = (a+b+c)/2
    if a > s or b > s or c > s:
        return 0
    area = math.sqrt(s*(s-a)*(s-b)*(s-c)) 
    return area

# A = [3,2,3,4]
# too slow
def solution(A):
    if len(A) == 3:
        a,b,c = A[0],A[1],A[2] 
        s = (a+b+c)/2
        if s>a and s>b and s>c and s != 0:
        # if heron_area(A[0],A[1],A[2]) != 0:
            return sum(A)
        else:
            return 0
    temp = []
    for subset in combinations(A,3):
        (a,b,c) = subset
        s = (a+b+c)/2
        # print(subset,sum(subset),heron_area(a,b,c))
        # if heron_area(a,b,c) != 0:
        if s>a and s>b and s>c and s != 0:
            temp.append(sum(subset))
    if temp:
        return max(temp)
    else:
        return 0

def solution2(A):
    A.sort()
    temp = []
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            temp.append(sum(A[i:i+3]))
    return max(temp) if temp else 0

def solution3(A):
    A.sort()
    for i in range(len(A)-1,1,-1):
        if A[i-2] + A[i-1] > A[i]:
            return sum(A[i-2:i+1]) 
    return 0



A = [1,1,5,2,3]
A2 = [2,1,2]
A3 = [3,2,3,4]
print(solution3(A3))




"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

def solution(n):
    way = {}
    way[1],way[2] = 1,2
    for i in range(3,n+1):
        way[i] = way[i-1] + way[i-2]
    return way[n]
    
n = 50
print(solution(n))
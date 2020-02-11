"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

def solution(n):
    import math
    integers = []
    if n % 2 != 0:
        for i in range(n):
            integers.append(i-math.floor(n/2))
    else:
        for i in range(int(n/2)):
            integers.append(i-(n/2))
        for i in range(int(n/2),int(n)):
            integers.append(i-(n/2)+1)
    return integers

n1,n2,n3 = 5, 8, 23
print(solution(n1))
print(solution(n2))
print(solution(n3))
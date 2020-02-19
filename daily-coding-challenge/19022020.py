"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
"""

def solution(n):
    fn = [0,1]
    for i in range(2,n+1):
        fn.append(fn[i-1]+fn[i-2])
    print(fn)
    return fn[n]

n = 30
print(solution(n))
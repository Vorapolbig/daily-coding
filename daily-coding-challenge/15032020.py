"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

def solution(n):
    dic = {}
    dic[0],dic[1],dic[2] = 0,1,1
    for i in range(0,n-2,1):
        dic[i+3] = dic[i] + dic[i+1] + dic[i+2]
    return dic[n]

print(solution(n=23))
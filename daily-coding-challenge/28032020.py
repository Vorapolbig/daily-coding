"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

def solution(x):
    if x == 0 or abs(x) > 2**31:
        return 0
    elif x < 0:
        x = -1*x
        if int(str(x)[::-1]) < 2**31: 
            return -1 * int(str(x)[::-1])
        else: 
            return 0
    else:
        if int(str(x)[::-1]) < 2**31:
            return int(str(x)[::-1])
        return 0

print(solution(1534236469))
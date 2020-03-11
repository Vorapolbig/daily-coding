"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""


def solution(x):
    return True if str(x) == str(x)[::-1] else False
    
x = 12321
print(solution(x))


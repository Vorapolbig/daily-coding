"""
Given an integer, write a function to determine if it is a power of two.
"""

def solution(n):
    if n <= 0:
        return False
    
    while n % 2 == 0:
        n //= 2
    return True if n == 1 else False

number = -16
print(solution(number))
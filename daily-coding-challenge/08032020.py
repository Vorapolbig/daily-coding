"""
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
"""

def solution(input):
    i = 1
    while i <= input:
        i = i << 1
    return (i-1) ^ input

input = 5
print(solution(input))
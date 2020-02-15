"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

"""

def solution(left,right):
    return [i for i in range(left, right + 1) if all(int(n) and not i % int(n) for n in str(i))]

left, right = 1, 21
print(solution(left,right))

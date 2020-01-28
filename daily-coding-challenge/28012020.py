"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

"""
def solution(input):
    product = 1
    for i in range(len(input)):
        product *= input[i]
    output = [product] * len(input)
    for i in range(len(input)):
        output[i] /= input[i]
    return output

test1 = [1, 2, 3, 4, 5]
test2 = [3, 2, 1]
print(solution(test2))

"""
with using division?
"""

def solution2(input):
    output = [1] * len(input)
    for i in range(len(input)):
        for j in range(len(input)):
            if i != j:
                output[i] *= input[j]
    return output

print(solution2(test1))
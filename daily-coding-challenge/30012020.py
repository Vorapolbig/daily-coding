"""
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

def solution(input):
    count = 1
    print(sorted(input))
    for i in sorted(input):
        if i > 0:
            if i == count:
                count += 1
                if i == sorted(input)[-1]:
                    return count
            else:
                return count

test1 = [3,4,-1,1]
test2 = [1,2,0]
test3 = [-1,-1,-2,3,4]
print(solution(test1))
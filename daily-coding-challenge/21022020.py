"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

nums = [1,2,3,2,3]
def solution(nums):
    nums_dict = {}
    for i, num in enumerate(nums):
        if num not in nums_dict:
            nums_dict[num] = 0
        else:
            nums_dict[num] += 1
    # print(nums_dict)
    for (k,v) in list(nums_dict.items()):
        if v == 0:
            return k
print(solution(nums))

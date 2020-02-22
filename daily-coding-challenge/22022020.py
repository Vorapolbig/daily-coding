"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def solution(nums):
    dic = {}
    for i, n in enumerate(nums):
        if not n in dic:
            dic[n] = 0
        else:
            dic[n] += 1
    
    for k,v in dic.items():
        if max(list(dic.values())) == v:
            return k
nums = [1,2,3,2,1,3,2]
print(solution(nums))

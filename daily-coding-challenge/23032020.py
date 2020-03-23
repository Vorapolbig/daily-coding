"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

def solution(nums):
    i = 0
    c = nums.count(0)
    while c != 0:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            c -= 1
            i -= 1
        i +=1
    return nums

def solution2(nums):
    i = 0
    for c in range(len(nums)):
        if nums[c] != 0:
            nums[c], nums[i] = nums[i], nums[c] 
            # print(nums)
            i+=1
    return nums


nums = [1,0,0,3,4,0,12,0]
# nums = [0,0,1]
print(solution2(nums))
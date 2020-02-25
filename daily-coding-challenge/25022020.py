"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

def solution(input):
    nums =  [0,1,0,3,12]
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[count] = nums[count], nums[i]
            # print(nums)
            count += 1 
    
    return nums


input: [0,1,0,3,12]
print(solution(input))
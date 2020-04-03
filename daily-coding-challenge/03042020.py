"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
def solution(nums):
    prev_sum = []
    cur_sum = 0
    for i in range(len(nums)):
        prev_sum.append(cur_sum)
        # print(i,cur_sum)
        # print(prev_sum)
        if cur_sum < nums[i]:
            cur_sum = 0
        cur_sum += nums[i]
    return max(prev_sum)

def solution2(nums):
    cur_sum = nums[0]
    max_sum = nums[0]

    for i in range(1,len(nums)):
        cur_sum = max(cur_sum+nums[i],nums[i])
        max_sum = max(cur_sum,max_sum)
    return max_sum

nums =  [-2,1,-3,4,-1,2,1,-5,4]
print(solution2(nums))
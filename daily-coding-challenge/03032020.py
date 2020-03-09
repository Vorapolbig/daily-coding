"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
"""

def solution(nums):
    output = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j:
                if nums[i] > nums[j]:
                    count += 1
        output.append(count)
    return output

def solution2(nums):
    output = []
    for i in range(len(nums)):
        output.append(sorted(nums).index(nums[i]))
    return output

nums = [8,1,2,2,3]
print(solution2(nums))

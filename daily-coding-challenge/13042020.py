"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

#runtime exceeded
def solution(nums):
    length = []
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            subarr = []
            for k in range(i,j+1):
                subarr.append(nums[k])
            if len(subarr)%2 == 0 and subarr.count(0) == len(subarr)/2:
                length.append(len(subarr))
    if len(length) == 0:
        return 0
    else:
        return max(length)


def solution2(nums):
    dic = {}
    subarr = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        elif nums[i] == 1:
            count += 1
        if count == 0:
            subarr = i+1
        if count in dic:
            subarr = max(subarr, i-dic[count])
        else: 
            dic[count] = i
        print(subarr)
    return subarr

# nums = [0,1]
nums = [0,0,1,0,0,0,1,1]
print(solution2(nums))
"""
1313. Decompress Run-Length Encoded List

We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are a elements with value b in the decompressed list.

Return the decompressed list.

"""

nums = [1,2,3,4]

def solution(nums):
    if len(nums) == 2:
        return [nums[1]] * nums[0]
    
    result = []

    for i, v in enumerate(nums):
        if i % 2 == 0:
            result += [nums[i + 1]] * v
    return result

print(solution(nums))

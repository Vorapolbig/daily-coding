"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


#Brute Force, Time limit Exceeded
def subarraySum(nums,k):
    n = 0
    for i in range(len(nums)):
        temp = 0
        for j in range(i,len(nums)):
            temp += nums[j]
            # if temp > k:
            #     break
            if temp == k:
                n += 1
    return n

nums = [1,1,1]
k = 2
# print(subarraySum(nums,k))

#  Time limit Exceeded
def subarraySum2(nums,k):
    dic = {}
    dic[0] = 0
    n = 0
    for i in range(0,len(nums)):
        dic[i+1] = dic[i] + nums[i]
    for i in range(len(nums)+1):
        for j in range(i+1,len(nums)+1):
            if dic[j]-dic[i] == k:
                print(j,i)
                n += 1
    print(dic)
    return n
        
def subarraySum3(nums,k):
    sumDict = {}
    sumDict[0] = 1
    n = 0
    cum = 0

    for num in nums:
        cum += num
        if cum - k in sumDict:
            n += sumDict[cum-k]
        if cum in sumDict:
            sumDict[cum] += 1
        else:
            sumDict[cum] = 1
        print(sumDict)
    return n

# nums = [1]
# nums = [1,2,4,5,1,-2,3,-4]
# k = 0
print(subarraySum3(nums,k))
""" 
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
def productExceptSelf(nums):
    output = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j != i:
                output[i] *= nums[j]
    return output


def productExceptSelf2(nums):
    product = 1
    for i in range(len(nums)):
        product *= nums[i] 
    output = []
    for i in range(len(nums)):
        output.append(int(product/nums[i]))
    return output

def productExceptSelf3(nums):
    out1 = [1]*len(nums)
    out2 = [1]*len(nums)
    for i in range(len(nums)-1):
        out1[i+1] = out1[i]*nums[i]
    for i in range(len(nums)-1,0,-1):
        out2[i-1] = out2[i]*nums[i]
    for i in range(len(nums)):
        out1[i] = out1[i] * out2[i]
    return out1

def productExceptSelf4(nums):
    out = [1]* len(nums)
    for i in range(1,len(nums)):
        out[i] = out[i-1]*nums[i-1]
    r = 1
    for i in range(len(nums)-1,-1,-1):
        out[i] = out[i] * r
        r *= nums[i]
    return out

nums = [1,2,3,4]
print(productExceptSelf4(nums))


  
"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""

def solution(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else: 
            dic[i] += 1
    dic.items()
    return [k for (k,v) in dic.items() if v == 2]


arr = [4,3,2,7,8,2,3,1]
print(solution(arr))
"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

"""

from collections import defaultdict
def solution(arr):
    minimum = 999999
    min_dict = defaultdict(list)
    output = []
    arr = sorted(arr)
    for i in range(1, len(arr)):
        # print(arr[i])
        if minimum >= arr[i] - arr[i-1]:
            minimum = arr[i] - arr[i-1]
            print(minimum)
            min_dict[minimum].append([arr[i-1],arr[i]])
            output.append([arr[i],arr[i-1]])
    return min_dict[minimum]

# arr = [ 1, 3, 4, 5]
# arr = [ 1, 3, 4, 6, 7, 8 ,10]
arr = [3,8,-10,23,19,-4,-14,27]
print(solution(arr))
    

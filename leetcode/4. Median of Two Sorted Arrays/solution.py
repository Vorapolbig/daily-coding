import math
nums1 = [1, 3]
nums2 = [2]
combine = nums1+nums2
combine = sorted(combine)
    # print(sorted(combine))
n = len(combine)
if n%2 != 0:    
    median = combine[int((n-1)/2)]
else:
    median = (combine[int(n/2)-1] + combine[int(n/2)])/2
print(median)
    
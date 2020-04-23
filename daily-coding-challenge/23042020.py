"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""

# time limited exceeded
def rangeBitwiseAnd(m,n):
    if m == 0:
        return 0
    if n-m <= 1:
        return m&n
    if n > 2**(len(bin(m))-1):
        n = 2**(len(bin(m))-1)
    ret = m
    for i in range(m+1,n+1):
        ret &= i
    return ret   

# use right shift 
def rangeBitwiseAnd2(m,n):
    count = 0
    while m != n:
        if n>m:
            n >>= 1
            m >>= 1
            count += 1
    for i in range(count):
        n <<= 1
    return n
            

# print(len(bin(2000))-2)
m,n = 5,7
# m,n = 1,4
# m,n = 600000000,2147483645
print(rangeBitwiseAnd2(m,n))
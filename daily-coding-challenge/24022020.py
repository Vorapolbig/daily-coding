"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

def solution(temp):
    n = len(temp)
    output = [0]*n
    max = -999999
    for i in range(n-1,-1,-1):
        print(i)
        if max <= temp[i]:
            max = temp[i]
        else:
            count = 1
            while temp[i+count] <= temp[i]:
                count += output[i+count]
            output[i] = count
    return output


temp = [73, 74, 75, 71, 69, 72, 76, 73]
print(solution(temp))
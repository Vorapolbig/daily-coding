"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

def solution(n):
    output = []
    for i in range(n):
        if len(output) == 0:
            output.append([1])
        elif len(output) == 1:
            output.append([1,1])
        else:
            sub = []
            sub.append(1)
            for j in range(len(output[i-1])-1):
                # print(output[i-1][j],output[i-1][j+1])
                sub.append(output[i-1][j]+output[i-1][j+1])
            sub.append(1)
            output.append(sub)
    return output

n = 5
print(solution(n))
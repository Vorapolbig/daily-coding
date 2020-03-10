"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.
"""

def solution(n,m,indices):
    rows, cols = [0]*n, [0]*m

    for i, j in indices:
        rows[i] += 1
        cols[j] += 1

    return sum((r+c) % 2 for r in rows for c in cols)

n,m = 2,3
indices = [[0,1],[1,1]]
print(solution(n,m,indices))
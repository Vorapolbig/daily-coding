"""

"""

from itertools import permutations

def solution(points):
    count = 0
    for combo in permutations(points,3):
        if dist(combo[0],combo[1]) == dist(combo[0],combo[2]):
            count += 1
    return count

def dist(A,B):
    return (A[0]-B[0])*(A[0]-B[0]) + (A[1]-B[1])*(A[1]-B[1])
    # return [abs(A[0]-B[0]),abs(A[1]-B[1])]


# points = [[0,0],[1,0],[2,0]]
points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
print(solution(points))
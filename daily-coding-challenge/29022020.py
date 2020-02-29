"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

"""
from itertools import combinations
def solution(points):
    return max(area(a,b,c) for a,b,c in combinations(points,3))

def area(a,b,c):
    return abs(1/2*(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1])))
    
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(solution(points))
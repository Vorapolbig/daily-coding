"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True

    for i in range(1,len(coordinates)):
        if coordinates[i][1] - coordinates[i-1][1] != 0 and coordinates[i][0]-coordinates[i-1][0] != 0:
            slope = (coordinates[i][1] - coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0])
            break
        
    for i in range(1,len(coordinates)):
        try:
            if (coordinates[i][1] - coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0]) != slope:
                return False
        except:
            pass
    return True
coordinates = [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]
# coordinates = [[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]
# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(checkStraightLine(coordinates))


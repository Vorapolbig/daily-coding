"""
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the point in the same order as they appear in the array.

"""
import numpy as np
#time limit exceed
def solution(points):
    counter = 0
    for i in range(len(points)-1):
        current_point = points[i]
        next_point = points[i+1]
        # print(current_point)
        # print(next_point)
        while current_point != next_point:
            all_moves = np.array([
                #vertically
                [current_point[0]+1,current_point[1]],
                [current_point[0]-1,current_point[1]],
                #horizontally
                [current_point[0],current_point[1]+1],
                [current_point[0],current_point[1]-1],
                #diagonally
                [current_point[0]+1,current_point[1]+1],
                [current_point[0]+1,current_point[1]-1],
                [current_point[0]-1,current_point[1]+1],
                [current_point[0]-1,current_point[1]-1]
            ])
            diff = all_moves - next_point
            distance = []
            for idx in range(len(diff)):
                distance.append(np.linalg.norm(diff[idx]))
            bestmove = all_moves[np.argmin(distance)]
            #update current point
            current_point = [bestmove[0],bestmove[1]]
            print(current_point)
            counter += 1
    return counter 

points = [[1,1],[3,4],[-1,0]]
print(solution(points))

def solution2(points):
    count = 0
    for i in range(len(points)-1):
        count += max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
    return count

points = [[1,1],[3,4],[-1,0]]
print(solution2(points))

    

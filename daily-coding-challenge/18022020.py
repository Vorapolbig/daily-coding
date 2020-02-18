"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

"""

def solution(height):
    step = 0
    for i, j in zip(heights, sorted(heights)):
        step += i != j
    return step

heights = [1,1,4,2,1,3]
print(solution(heights))
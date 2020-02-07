"""
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. 
Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 
"""
import collections

def solution(groupSize):
    group = collections.defaultdict(list)
    group_dict = {}

    for person_id, size in enumerate(groupSize):
        if size not in group_dict:
            group_dict[size] = (size,0)

        if len(group[group_dict[size]]) == size:
            group_dict[size] = (group_dict[size][0], group_dict[size][1]+1)

        group[group_dict[size]].append(person_id)

    return list(group.values())


groupSize = [3,3,3,3,3,1,3]
print(solution(groupSize))
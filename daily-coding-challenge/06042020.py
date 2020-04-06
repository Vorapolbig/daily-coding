"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""

# def solution(strs):
#     output = []
#     for s1 in strs:
#         # print(s1)
#         sub = [s1] * strs.count(s1)
#         if strs.count(s1) > 1:
#             strs.reverse()
#             for i in range(strs.count(s1)-1):
#                 strs.remove(s1)
#             strs.reverse()
#         # print(strs)
#         for s2 in strs:
#             print(strs)
#             print(s1,'and',s2)
#             if isSimilar(s1,s2) and s1 != s2:
#                 sub.append(s2)
#                 strs.remove(s2)
#                 # print(sub)
#         output.append(sub)
#         # strs.remove(s1)
#     return output

def solution(strs):
    dic = {}
    for s in strs:
        if "".join(sorted(s)) in dic:
            dic["".join(sorted(s))].append(s)
        else:
            dic["".join(sorted(s))] = [s]
    return list(dic.values())
            

# def isSimilar(s1,s2):
#     if len(s1) != len(s2) or set(s1) != set(s2) or sorted(list(s1)) != sorted(list(s2)):
#         return False
#     else:
#         return True

# strs = ["",""]
# strs = ["","b",""]
strs = ["eat", "tea", "tan", "ate", "nat", "bat","bat"]
# strs = ["ate","eat","tea"]
print(solution(strs))
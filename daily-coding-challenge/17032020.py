"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""

s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car"
def solution(s,t):
    if len(s) != len(t):
        return False
    # if set(s) - set(t):
    #     return False
    list1 = list(s)
    list2 = list(t)
    for i in list1:
        if i not in list2:
            return False
        else:
            list2.remove(i)
    return True

def solution2(s,t):
    if len(s) != len(t):
        return False
    list1 = sorted(list(s))
    list2 = sorted(list(t))
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

def solution3(s,t):
    return sorted(s) == sorted(t)

def solution4(s,t):
    for i in range(97,123):
        if s.count(chr(i)) != t.count(chr(i)):
            return False
    return True
    
    

print(solution4(s,t))
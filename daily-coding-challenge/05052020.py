"""
"""

s = "dddccdbba"
def solution(s):
    if len(s) == 0:
        return -1
    dic = {}
    for i, char in enumerate(s):
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    try:
        char_out = (list(dic.keys())[list(dic.values()).index(1)])
        return s.index(char_out)
    except:
        return -1

print(solution(s))
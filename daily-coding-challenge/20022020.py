"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
"""

def solution(S):
    c = 0
    s = 0
    out = ""
    for i,p in enumerate(S):
        # print(i,p,c)
        if p == "(":
            c += 1
        else:
            c -= 1
        if c == 0:
            x = S[s:i+1][:-1][1:]
            out += x
            s = i+1
    return out

S = "(()())(())"
print(solution(S))
        
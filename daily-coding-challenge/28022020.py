"""
We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.
"""

def solution(widths, S):
    a=0
    b=1
    for c in S:
        if a <=100-widths[ord(c)-97]:
            a+=widths[ord(c)-97]
        else:
            b+=1
            a=0
        a+=widths[ord(c)-97]
    return [b,a]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
print(solution(widths, S))
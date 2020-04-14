"""
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
"""
def solution(s,shift):
    right = sum([y for [x,y] in shift if x == 1])
    left = sum([y for [x,y] in shift if x == 0])
    move = right-left
    print(move)
    if move > len(s):
        move = move%len(s)
    if move < -len(s):
        move = -abs(move)%len(s)
    return s[-move:] + s[:-move]
# s = "abcdefg"
# shift = [[1,1],[1,1],[0,2],[1,3]]
# s = "abc"
# shift = [[0,1],[1,2]]
# s = "joiazl"
# shift = [[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]
# s = "wpdhhcj"
# shift = [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]
s = "xqgwkiqpif"
shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
print(solution(s,shift))
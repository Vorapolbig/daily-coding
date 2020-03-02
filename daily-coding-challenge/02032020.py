"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""

def solution(s):
    front = 0
    back = len(s)-1
    while front < back:
        print(front,back)
        swap(s,front,back)
        front += 1
        back -= 1
    return s

def swap(s,front,back):
    temp = s[front]
    s[front] = s[back]
    s[back] = temp

s = ["h","e","l","l","o"]
print(solution(s))

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

def solution(s):
    reverse = {'}':'{', ']':'[',')':'('}
    stack = []
    for i in s:
        if i in reverse.values():
            stack.append(i)
        else:
            try:
                if stack[-1] == reverse[i]:
                    stack.pop()
                else: 
                    return False
            except: 
                return False
    if stack == []:
        return True
    else: return False

s = '()[]{}'
print(solution(s))
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
def isPalindrome(s):
    special = []
    for string in s:
        if not string.isalpha() and not string.isdigit():
            special.append(string)
    s = s.lower()
    for string in special:
        s = s.replace(string,"")
    # print(s[::-1])
    return s == s[::-1]
"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

"""

def solution(string):
    count = 0
    balance = 0
    for s in string:
        if s == 'R':
            count += 1
        else:
            count -= 1
        if count == 0:
            balance += 1    
    return balance

string = "RLLLLRRRLR"
string2 = "RLRRRLLRLL"
print(solution(string2))
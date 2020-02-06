"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

def solution(J, S):
    jewels = []
    count = 0
    for i in J:
        jewels.append(i)
    for i in S:
        if i in jewels:
            count += 1
    
    return count

J = "aA"
S = "aAAbbbb"

print(solution(J,S))
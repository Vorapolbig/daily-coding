"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

def solution(number):
    all_number = []
    all_number.append(number)
    for i, n in enumerate(str(number)):
        temp = list(str(number))
        if n == "6":
            temp[i] = '9'
        elif n == "9":
            temp[i] = '6'
        all_number.append(int("".join(temp)))

    return max(all_number)

number =9669
print(solution(number))
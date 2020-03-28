"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""
def solution(left,right):
    output = []
    for number in range(left,right+1,1):
        c = 0
        for i in str(number):
            if int(i) != 0 and number % int(i) == 0 and c >= 0:
                c += 1
            else:
                c = -1
            if c == len(str(number)):
                output.append(number)
    return output

def solution2(left,right):
    output = []
    for number in range(left,right+1,1):
        for id, i in enumerate(str(number)):
            if int(i) == 0 or number % int(i) != 0:
                break
            if id == len(str(number))-1:
                output.append(number)
    return output


print(solution2(1,22))
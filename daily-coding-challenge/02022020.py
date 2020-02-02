"""
This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def solution(message):
    n = len(message)
    dp = [0 for i in range(n+1)]

    for i in range(1,n+1):
        if i == 1:
            if message[i-1] != '0':
                dp[0] = 1
                dp[1] = 1
        if i >= 2:
            if message[i-1] != '0':
                dp[i] += dp[i-1]

            if 10 <= int(message[i-2:i]) <= 26:
                dp[i] += dp[i-2] 
    return dp[-1]

print(solution("2263"))
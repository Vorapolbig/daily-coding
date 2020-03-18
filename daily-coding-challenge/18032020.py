"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
prices = [7,1,5,3,6,4]

#Brute Force
def solution(prices):
    profit = []
    for i in range(len(prices)):
        for j in range(len(prices)):
            if i < j:
                profit.append(prices[j]-prices[i])
    if len(profit) > 0 and max(profit) > 0:
        return max(profit)
    else:
        return 0

print(solution(prices))
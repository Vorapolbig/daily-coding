"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
prices = [7,1,5,3,6,4]

#Brute Force
def solution(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if i < j and prices[j]-prices[i] > profit:
                profit = prices[j]-prices[i]
    return profit

def solution2(prices):
    min_price = 99999999
    profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > profit:
            profit = prices[i] - min_price
    return profit

#DP
def solution3(prices):
    min_price = 999999
    profit = 0
    for price in prices:
        min_price = min(min_price,price)
        profit = max(profit, price-min_price)
    return profit






print(solution3(prices))
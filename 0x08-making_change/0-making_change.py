#!/usr/bin/python3
"""coins of different values,"""


def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Create an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    # the base case: 0 coin
    dp[0] = 0
    # Iterate through each coin
    for coin in coins:
        # Update the dp array for amounts that can be reached with this coin
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means we cannot make that amount
    return dp[total] if dp[total] != float('inf') else -1

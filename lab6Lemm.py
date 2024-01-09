from time import time

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0:  # The base case
        return 0
    else:  # The recursive case
        minCoins = float("inf")
        for currentCoin in coins:  # Check all coins
            # If we can give change
            if (amount - currentCoin) >= 0:
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
                # Keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins

# Algorithm 2: Dynamic Programming with traceback
def DPcoins(coins, amount):
    # Create the initial tables
    dp = [0] + [float("inf")] * amount
    traceback = [-1] * (amount + 1)

    # Fill in the base case(s)
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                traceback[i] = coin

    # Perform the traceback to print result
    if dp[amount] != float("inf"):
        temp_amount = amount
        while temp_amount > 0:
            print(traceback[temp_amount])
            temp_amount -= traceback[temp_amount]

    return dp[amount]  # return optimal number of coins


C = [1,5,10,12,25]  # same denominations
A = int(input('Enter desired amount of change: '))
assert A>=0
print("DAC:")
t1 = time()
numCoins = DACcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
print()
print("DP:")
t1 = time()
numCoins = DPcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")



##### OUTPUT #####
# Enter desired amount of change: 29
# DAC:
# optimal: 3  in time:  7.5 ms

# DP:
# 12
# 12
# 5
# optimal: 3  in time:  0.0 ms
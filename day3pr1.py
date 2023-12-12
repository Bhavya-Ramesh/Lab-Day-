def max_profit(prices):
    if not prices:
        return 0
    n = len(prices)
    k = 2  
    dp = [[0] * n for _ in range(k + 1)]
    for i in range(1, k + 1):
        max_diff = -prices[0]  
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])
    return dp[k][n - 1]
stock_prices = [3, 2, 6, 5, 0, 3]
result = max_profit(stock_prices)
print(result)

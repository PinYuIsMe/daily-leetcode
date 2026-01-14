class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # n = len(coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(0, amount + 1):
            if dp[i] == amount + 1:
                continue
            for j in coins:
                if i + j <= amount:
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
        
        return dp[-1] if dp[-1] != (amount + 1) else -1
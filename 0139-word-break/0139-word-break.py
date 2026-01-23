class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        maxLen = max(len(word) for word in wordDict) if wordDict else 0
        n = len(s)
        print(f"maxLen: {maxLen}")

        # construct dp table
        dp = [False for _ in range(n+1)]
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i-1, max( -1, i - maxLen - 1), -1):

                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]
        
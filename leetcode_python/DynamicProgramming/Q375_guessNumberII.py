import sys


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * n for i in range(n)]
        for j in range(n):
            for i in range(j, -1, -1):
                if i != j:
                    dp_i_j = min(i + 1 + dp[i + 1][j], j + 1 + dp[i][j - 1])
                    for k in range(i + 1, j):
                        dp_i_j_k = max(k + 1 + dp[i][k - 1], k + 1 + dp[k + 1][j])
                        dp_i_j = min(dp_i_j, dp_i_j_k)
                    dp[i][j] = dp_i_j
        return dp[0][n - 1]

print(Solution().getMoneyAmount(10))
# n, m = map(int, input().split())
#
# dp = [([0]*52) for _ in range(52)]
#
# dp[0][1] = 0
# dp[1][0] = 0
# dp[1][1] = 1
#
# for i in range(2, n+1):
#     for j in range(2, m+1):
#         dp[i][j] = dp[i-1][j+2] + dp[i+1][j+2] + dp[i+2][j+1] + dp[i+2][j-1]
#         print(dp[i][i])
# print(dp[i][j])


# n = int(input())
#
# L = list(map(int, input().split()))
#
# dp = [0] * 1005
#
# dp[0] = 1
#
# for i in range(1, n):
#     for j in range(i-1, 0, -1):
#         if L[i] > L[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#             print(dp[i])
#
#
# print(max(dp))

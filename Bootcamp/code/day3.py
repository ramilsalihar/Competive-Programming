# a, b = map(int, input().split())
#
# n, m = map(int, input().split())
#
# dp = [[0] * (m + 1)] * (n + 1)
# dp[1][1] = 1
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
# print(dp[n][m])


# Самый дешевый путь

n, m = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

dp = [[0]*25]*25
dp[1][1] = a[0][0]
ans = 0
for i in range(1, n):
    for j in range(2, m):
        dp[i][j] += dp[i][j-1]
        print(dp[i][j])
    dp[j][i] += dp[j][i-1]
    print(dp[j][i])
    if dp[j][i] > dp[i][j]:
        ans += dp[i][j]
    else:
        ans += dp[j][i]

# print(ans)
print(a)
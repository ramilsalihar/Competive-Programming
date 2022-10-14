# n = int(input())
# pos = sorted(list(map(int, input().split())))
#
# dp = [0]*(10005)
#
# dp[2] = pos[2] - pos[1]
# dp[3] = pos[3] - pos[1]
# dp[4] = (pos[4] - pos[3]) + (pos[2] - pos[1])
#
# if n > 4:
#     for i in range(5, n+1):
#         dp[i] = min(dp[i-2] + pos[i] - pos[i-1], dp[i-3] + pos[i] - pos[i-2])
# print(dp[n])

# Abduzhabbarov, [12 / 20 / 2021 3: 19
n = int(input())
a = [0] + sorted(list(map(int, input().split())))
dp = [0] * 105
dp[1] = 0
if n >= 2:
    dp[2] = a[2] - a[1]
if n >= 3:
    dp[3] = a[3] - a[1]
if n >= 4:
    dp[4] = a[4] - a[3] + a[2] - a[1]

for i in range(5, n + 1):
    dp[i] = min(dp[i - 2] + a[i] - a[i - 1], dp[i - 3] + a[i] - a[i - 2])

print(dp[n])





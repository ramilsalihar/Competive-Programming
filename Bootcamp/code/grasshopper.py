import math
n, k = map(int, input().split())

if k >= n:
    k = n-1
elif k == 1:
    ans = 1
else:
    dp[1,1]
    for i in range(2, n):
        dp.append(sum(dp[-k:]))


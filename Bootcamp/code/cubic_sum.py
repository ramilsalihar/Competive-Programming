n = int(input())

dp = [0]*(10**6)
for i in range(n):
    x = 0
    while x*x*x < n:
        dp[i] = min(dp[i], dp[i-(x**3)] + 1)
        x += 1

print(dp[n])
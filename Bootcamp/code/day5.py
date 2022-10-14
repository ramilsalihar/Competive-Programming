# A

n = int(input())
L = list(map(int, input().split()))

dp = [0]*40000
dp[0] =


# B
n = int(input())

c = [0] + list(map(int, input().split()))
dp = [0]*(10**5)

if n == 1:
    print(0)

dp[0] = 0
dp[1] = c[1] - c[0]



for i in range(2, n+1):
    dp[i] = min(dp[i-1] + abs(c[i] - c[i-1]), dp[i-2] + abs(c[i] - c[i-2]))

print(dp[n-1])

a = input()
b = input()

dp = [[0]*1005 for _ in range(1005)]

dp[0][0] = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] != b[j]:
            dp[i][j] = min(dp[i-1][j]+1, dp[j-1][i]+1, dp[i-1][j-1]+1)
        else:
            dp[i][j] = min(dp[i - 1][j] + 1, dp[j - 1][i] + 1, dp[i - 1][j - 1])
for i in dp[:10]:
    print(i[:10])
print(dp[len(a)-1][len(b)-1])

from sys import stdin, stdout

s1 = ' ' + stdin.readline()[:-1]
s2 = ' ' + stdin.readline()[:-1]

dp = [[0] * (len(s1) + 5) for _ in range(len(s2) + 5)]
dp[0] = list(range(len(s1) + 5))
for i in range(len(s2) + 5):
    dp[i][0] = i
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min([dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]]) + 1
stdout.write(str(dp[len(s1) - 1][len(s2) - 1]))
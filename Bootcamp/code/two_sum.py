from sys import stdin, stdout

final = int(stdin.readline())

cnt = {}
cnt[1] = 2
cnt[2] = 4

for i in range(3, final + 1):
    cnt[i] = cnt[i - 1] + cnt[i - 2]
print(cnt[final])
# n, s = map(int, input().split())
#
# L = []
# for _ in range(n):
#     L.append(list(map(int, input().split())))
#
# deg = [[] for _ in range(105)]
# ans = 0
# K = [False]*105
# def dfs(v):
#     global ans, K, L
#     K[v] = True
#     ans += 1
#     for i in L[v]:
#         if not K[i]:
#           dfs(i)
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if L[j-1] == 1:
#             deg[i].append(j)
#
# dfs(s)
# print(L)
# # print(K)
# print(ans)


from sys import stdin, stdout

result = 0
n, s = map(int, stdin.readline().split())

a = [[] for _ in range(105)]

visited = [False] * 105

for i in range(1, n + 1):
    row = list(map(int, stdin.readline().split()))
    for j in range(1, n + 1):
        if row[j - 1] == 1:
            a[i].append(j)


def dfs(v):
    global result, visited, a
    visited[v] = True
    result += 1
    for i in a[v]:
        if not visited[i]:
            dfs(i)


dfs(s)
stdout.write(str(result))








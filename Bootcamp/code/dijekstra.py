# from sys import stdin, stdout
#
# n, s, f = map(int, stdin.readline().split())
#
# g = [[]]
#
# for _ in range(n):
#     g.append([0] + list(map(int, stdin.readline().split())))
#
# print(g)
#
#
# distance = [int(1e6)] * (n + 5)
# distance[s] = 0
# p = []
# q = set()
# q.add((0, s))
#
# while q:
#     v = min(q)[1]
#     q.discard(min(q))
#     for j in range(1, n + 1):
#         if g[v][j] <= 0:
#             continue
#         if distance[v] + g[v][j] < distance[j]:
#             q.discard((distance[j], j))
#             distance[j] = distance[v] + g[v][j]
#             q.add((distance[j], j))
#
# if distance[f] == int(1e6):
#     stdout.write('-1')
# else:
#     stdout.write(str(distance[f]))


from heapq import *

INF = 1 << 60
s, f = map(int, input().split())
n, m = map(int, input().split())
g, d, p, q = [[] for _ in range(n)], [0] + [INF] * n, [-1] * n, [(0, 0)]
for _ in range(m):
    u, v, t = map(int, input().split())
    g[u - 1] += [(t, v - 1)]
    g[v - 1] += [(t, u - 1)]
while q:
    u = heappop(q)[1]
    for e in g[u]:
        t, v = d[u] + e[0], e[1]
        if t < d[v]:
            d[v], p[v] = t, u
            heappush(q, (d[v], v))
if d[n - 1] == INF:
    print(-1);
else:
    x, a = n - 1, []
    while x != -1:
        a += [x + 1]
        x = p[x]
    a.reverse()
    print(d[n-1])
    print(' '.join(map(str, a)))
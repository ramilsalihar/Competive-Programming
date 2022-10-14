# n, m = map(int, input().split())
#
# L = []
# for _ in range(n):
#     L.append(list(map(int, input().split())))
#
# print(L)

# # creating a queue
# q = []
# v = []
#
# # mark v as visited and put v into Q
# def dfs(visited, L, node):
#     visited.append(node)
#     q.append(node)
#
#     while q:
#         m = q.pop(0)
#         for i in



n, m = map(int, input().split())
s, f = map(int, input().split())

L = []
for _ in range(m):
    L.append([0] + list(map(int, input().split())))

distance = [int(1e6)] * (n + 5)
distance[s] = 0
q = set()
q.add((0, s))
p = [-1]*(10)
p[1] = 0

while q:
    v = min(q)[1]
    q.discard(min(q))
    for j in range(1, n):
        to = L[v][j]
        if L[v][j] <= 0:
            continue
        if distance[v] + L[v][j] < distance[j]:
            q.discard((distance[j], j))
            distance[j] = distance[v] + L[v][j]
            q.add((distance[j], j))
            p[to] = v


if distance[f-1] == int(1e6):
    print("-1")
else:
    x, a = n-1 , []
    while x != -1:
        a += [x+1]
        x = p[x]
    a.reverse()
    print((str(distance[f - 1])))
    print(' '.join(map(str, a)))



n, m, k = map(int, input().split())

apart_size = sorted(list(map(int, input().split())))
apart = sorted(list(map(int, input().split())))

sorted(apart_size)
sorted(apart)

i = j = 0
res = 0
while i < n and j < m:
    if apart[j] in range(apart_size[i] - k, apart_size[i] + k +1):
        res += 1
        i += 1
        j += 1
    elif apart[j] > apart_size[i]:
        i += 1
    elif apart[j] < apart_size[i]:
        j += 1
print(res)


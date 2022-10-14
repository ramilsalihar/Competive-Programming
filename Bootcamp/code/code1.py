# import math
#
# n = int(input())
#
# for _ in range(n):
#     m = int(input())
#     k = int(math.sqrt(m))
#     l = []
#     for i in range(k+1):
#         if ((i**2) <= m):
#             l.append(i**2)
#         if ((i**3) <= m):
#             l.append(i**3)
#     print(int(len(set(l))-1))


n = int(input())

def sub(a, s):
    b = 0
    x = len(s)
    y = len(a)
    if (int(s[-1]) - int(a[-1])) >= 0:
        b += (int(s[-1]) - int(a[-1]))
        s = s[:-1]
        a = a[:-1]
    elif (int(s[-1]) - int(a[-1])) < 0:
        b += (int(s[n-2:]) - int(a[-1]))
        s = s[:-2]
        a = a[:-1]
    return b

for _ in range(n):
    a, s = input().split()



def find(a, s):
    a = list(a)
    s = list(s)
    b = ""
    if len(a) > len(s):
        return -1
    elif (int(s[-1]) - int(a[-1])) < 0:
        b += str((int(s[-2:]) - int(a[-1])))
        return find(a[:-2], s[:-1])
    elif (int(s[-1]) - int(a[-1])) > 0:
        b += str((int(s[-1:]) - int(a[-1])))
        return find(a[:-1], s[:-1])
    return b[::-1]


print(find("17236","1106911"))


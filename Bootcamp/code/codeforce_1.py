# # A
#
# t = int(input())
#
# L = []
# for _ in range(t):
#     L.append(input())
#
# for i in L:
#     if ("N" in i):
#         if i.count("N") == 1:
#             print("NO")
#         else:
#             print("YES")
#     else:
#         print("YES")
#

# B


# # for y max
# def max_y(O_ver, h_ver):
#     y1 = max(h_ver) - min(h_ver)
#     y2 = max(O_ver) - min(O_ver)
#     return max(y1, y2)
#
# # for x max
# def max_x(O_hor, h_hor):
#     x1 = max(h_hor) - min(h_hor)
#     x2 = max(O_hor) - min(O_hor)
#     return max(x1, x2)
#
# def biggest(max_x, max_y):
#     a = 0
#     b = 0
#     if max_x > max_y:
#         a = max_x
#         b = h
#     elif max_x == max_y:
#         a = max_x
#         if w >= h:
#             b = w
#     else:
#         a = max_y
#         b = w
#     return a, b
#
# t = int(input())
#
# for _ in range(t):
#     w, h = map(int, input().split())
#     O_hor = list(map(int, input().split()))
#     h_hor = list(map(int, input().split()))
#     O_ver = list(map(int, input().split()))
#     h_ver = list(map(int, input().split()))
#     O_hor = O_hor[1:]
#     h_hor = h_hor[1:]
#     O_ver = O_ver[1:]
#     h_ver = h_ver[1:]
#     height, width = biggest(max_x(O_hor, h_hor), max_y(O_ver, h_ver))
#     Area = height * width
#     print(Area)
#

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    O_hor = list(map(int, input().split()))
    h_hor = list(map(int, input().split()))
    O_ver = list(map(int, input().split()))
    h_ver = list(map(int, input().split()))
    a1 = (O_hor[-1] - O_hor[1])*h
    a2 = (h_hor[-1] - h_hor[1])*h
    a3 = (O_ver[-1] - O_ver[1])*w
    a4 = (h_ver[-1] - h_ver[1])*w
    print(max(a1, a2, a3, a4))
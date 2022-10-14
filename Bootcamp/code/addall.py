# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     k = sum(a)
#     if (sum(a) % n) == 0:
#         print("0")
#     else:
#         print("1")



def decimalToBinary(n):
    return bin(n).replace("0b","")


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = int(binary) % 10
        decimal = decimal + dec * pow(2, i)
        binary = int(binary) // 10
        i += 1
    return decimal

# l, r = map(int, input().split())
# for i in range(l-1, r+1):
#     print(decimalToBinary(i))
# n = int(13, 2)
# print(n)

"""B"""

# t = int(input())
#
#
def decimalToBinary(n):
    return bin(n).replace("0b","")


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = int(binary) % 10
        decimal = decimal + dec * pow(2, i)
        binary = int(binary) // 10
        i += 1
    return decimal

print(decimalToBinary(23))
#
#
# for _ in range(t):
#     l, r = map(int, input().split())
#     L = list(decimalToBinary(r))
#     print(L)
#     for i in L:
#         k = r - 1
#         while k != l:
#             M = list(decimalToBinary(k))
#             for j in M:
#                 if i != j:
#                     if len(L) >= len(M):
#                         i = j
#                         continue
#                     k -= 1
#
#     strs = [str(int) for int in L]
#     ans = "".join(strs)
#     print(binaryToDecimal(ans))

# def burning(l1):
#     k = set(l1)
#     m = k.pop()
#     print(k)
#     print(m)
#     if len(k) == 1 and m == "0":
#         return True
#     return False
#
#
# L = [0, 0]
#
# print(burning(L))
# a, b = 100000, 200000
# for i in range(a-1, b+1):
#     print(i&(i-1))




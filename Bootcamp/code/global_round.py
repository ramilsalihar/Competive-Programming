# def compare(l1, l2):
# #    for i in range(min(len(l1), len(l2))):
# #        if l1[i] != l2[i]:
# #            return False
# #        else:
# #            return len(l1) == len(l2)
# #
# # def burning(l1):
# #     k = set(l1)
# #     if len(k) == 1 and "0" in k:
# #         return True
# #     return False
# #
# #
# # t = int(input())
# # for _ in range(t):
# #     n = int(input())
# #     a = list(input())
# #     b = list(input())
# #     if compare(a, b):
# #         print(0)




# prime = [True for i in range(a, b+1)]
# p = 2
# for p in range(p*p, b):
#     if prime[p] == True:
#         for i in range(p*p, b+1, p):
#             prime[i] = False
#     p += 1
#
# print(prime)
#
# for p in range(2, b+1):
#     if prime[p-2]:
#         print(p)


# def PrimeChecker(a):
#     if a > 1:
#         for j in range(2, int(a/2) + 1):
#             if (a % j) == 0:
#                 return False
#                 break
#         else:
#             return True
#     else:
#         return False
#
# a, b = map(int, input().split())
#
# prime = [True for i in range(b + 1)]
# p = 2
# while (p * p <= b):
#     if (prime[p] == True):
#         for i in range(p+p, b + 1, p):
#             prime[i] = False
#     p += 1
#
# L = []
# for j in range(a, b + 1):
#     if prime[j]:
#         if j == 1:
#             continue
#         else:
#             L.append(j)
#
#
# R = []
# for i in L:
#     k = str(i)[::-1]
#     R.append(int(k))
#
# ans = 0
# for i in R:
#     if PrimeChecker(i):
#         ans += 1
#
# print(ans)


# def decimalToBinary(n):
#     return bin(n).replace("0b","")
#
# n = int(input())
# w = ""
# k = list(decimalToBinary(n))
# for i in k:
#     if i == "1":
#         w += "SX"
#     else:
#         w += "S"
# print(w[2:])


    n = int(input())

    import math
    def primefactors(n):
        L = []
        # while n % 2 == 0:
        #     L.append(2)
        #     n = n / 2

        for i in range(2, int(math.sqrt(n)) + 3):
            while (n % i == 0):
                L.append(i)
                n = n / i
        if n > 1:
            L.append(int(n))
        return L

    ans = []
    for j in primefactors(n):
        ans.append(str(j))
        ans.append("*")

    l = ''.join(ans[:-1])

    print(l)

n, m = map(int, input().split())
L = []
for _ in range(m):
    L.append(list(map(int, input().split())))




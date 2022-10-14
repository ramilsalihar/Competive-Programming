# t = int(input())
#
# nums = list(map(int, input().split()))
#
#
# def merge(A, B):
#     res = []
#     i = 0
#     j = 0
#     while i<len(A) and j<len(B):
#         if A[i] <= B[j]:
#             res.append(A[i])
#             i += 1
#         else:
#             res.append((B[j]))
#             j += #     return res
#
#
# def MergeSort(A):
#     if len(A) <= 1:
#         return A
#     else:
#         L = A[:len(A)//2]
#         R = A[len(A)//2:]
#     return merge(MergeSort(L), MergeSort(R))
#
# print(MergeSort(nums))

# D
word = list(input())
check = list(input())



W = []
for i in word:
    W.append(i)
    W.append(word.count(i))
    word.remove(i)

C = []
for i in check:
    C.append(i)
    C.append(word.count(i))
    check.remove(i)

print(W, C)
print(word, check)
# if (W[::2] == C[::2]) and (W[1::2] == C[1::2]):
#     print("YES")
# else:
#     print("NO")



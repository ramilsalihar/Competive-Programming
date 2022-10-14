# MERGE SORT


"""
1. If a = b, do not do anything, because a subarray that only contains one element
is already sorted.
2. Calculate the position of the middle element: k =[(a + b)/2]
3. Recursively sort the subarray array[a . . . k].
4. Recursively sort the subarray array[k + 1 . . . b].
5. Merge the sorted subarrays array[a . . . k] and array[k + 1 . . . b] into a sorted
subarray array[a . . . b].
"""
# Time complexity O(n)


t = int(input())

nums = list(map(int, input().split()))


def merge(A, B):
    res = []
    i = 0
    j = 0
    while i<len(A) and j<len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append((B[j]))
            j += 1
    res += A[i:] + B[j:]
    return res


def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[:len(A)//2]
        R = A[len(A)//2:]
    return merge(MergeSort(L), MergeSort(R))

print(MergeSort(nums))


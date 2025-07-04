def counting_sort(A,k):
    n = len(A)
    B = [None] * n
    C = [0] * 26
    for x in A:
        print(C[ord(x[k]) - ord("a")])
        C[ord(x[k]) - ord("a")] += 1
    for i in range(1,26):
        C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        B[C[ord(A[i][k]) - ord("a")] - 1] = A[i]
        C[ord(A[i][k]) - ord("a")] -= 1
    for i in range(n):
        A[i] = B[i]

def radix_sort(T):
    n = len(T[0])
    for i in range(n-1,-1,-1):
        counting_sort(T,i)
    print(T)

T = ["aab","ddc","vax","acb","bac","cba"]
radix_sort(T)
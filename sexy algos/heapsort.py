def heapify(A,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,n,max_ind)

def build_heap(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        heapify(A,n,i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A,i,0)
 
T = [15,3,6,4,16]
heap_sort(T)
from kolutesty import runtests

def ice_cream( T ):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    k = 0
    S = 0
    maxi = float("-inf")
    B = [0 for _ in range(n)]

    for i in range(n):
        if T[i] < n:
            B[T[i]] += 1
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )

from kol2atesty import runtests

INF = float('inf')

def drivers( P, B ):
    # tu prosze wpisac wlasna implementacje
    n = len(P)
    for i in range(n):
        P[i] = [P[i][0],P[i][1],i]
    P = sorted(P, key = lambda x: x[0])
    D = []
    pk = 0

    for i in range(1,n):
        if P[i][1]:
            D.append([pk, P[i][2]])
            pk = 0
        else: pk += 1

    m = len(D)
    F = [[[INF for _ in range(m+1)] for _ in range(3)] for _ in range(2)] # F[k][e][i]
    T = [[[[] for _ in range(m+1)] for _ in range(3)] for _ in range(2)]
    F[0][2][1] = 0

    for i in range(2,m+1):
        for e in range(3):
            for k in range(2):
                if e < 2:
                    F[k][e][i] = F[k][e+1][i-1] + D[i-1][0]*k
                    T[k][e][i] = T[k][e+1][i-1]
                else:
                    for e2 in range(3):
                        if F[1-k][e2][i-1] + D[i-1][0]*k < F[k][e][i]:
                            F[k][e][i] = F[1-k][e2][i-1] + D[i-1][0]*k
                            T[k][e][i] = T[1-k][e2][i-1] + [D[i-2][1]]

    minI = INF
    res = []
    for e in range(3):
        for k in range(2):
            if minI > F[k][e][m]:
                minI = F[k][e][m]
                res = T[k][e][m]

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )

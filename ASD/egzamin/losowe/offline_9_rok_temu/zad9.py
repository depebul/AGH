from zad9testy import runtests

def mapArray(T,C,L):
    for _ in range(len(T)):
        T[_]=(C[_],T[_])
    T.append((0,0))
    T.append((0,L))
    T.sort(key=lambda x: x[1])
    return T
def min_cost( O, C, T, L ):
    O=mapArray(O,C,L)
    n=len(O)
    dp=[[float('inf') for _ in range(2)]for _ in range(n)]
    dp[0][0]=0
    dp[0][1]=0
    if T >=L:
        return 0
    for station in range(1,n):
        for neighbour in range(station,-1,-1):
            if O[station][1]-O[neighbour][1]<=T:
                dp[station][0]=min(dp[station][0],dp[neighbour][0]+O[station][0])
                dp[station][1]=min(dp[station][1],dp[neighbour][1]+O[station][0])
            elif O[station][1]-O[neighbour][1]<=2*T:
                dp[station][1]=min(dp[station][1],dp[neighbour][0]+O[station][0])

    return min(dp[n-1][0],dp[n-1][1])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

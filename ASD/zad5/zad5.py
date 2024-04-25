from zad5testy import runtests

E = [(0,1, 5),
     (1,2,21),
     (1,3, 1),
     (2,4, 7),
     (3,4,13),
     (3,5,16),
     (4,6, 4),
     (5,6, 1)]
S = [ 0, 2, 3 ]
a = 1
b = 5
n = 7


def spacetravel( n, E, S, a, b ):
    n = max(E, key=lambda x: x[1])[1] + 1
    neighbours = [[] for _ in range(n)]
    if a in S and b in S:
        return 0
    elif a in S:
        name = a
    elif b in S:
        name = b
    else:
        name = S[0]
    brolist = []
    for i in range(len(E)):
        if E[i][0] not in S:
            continue

    print(E)
    for i in range(len(E)):
        neighbours[E[i][0]].append([E[i][1], E[i][2]])
        neighbours[E[i][1]].append([E[i][0], E[i][2]])



spacetravel( n, E, S, a, b )
# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( spacetravel, all_tests = False )
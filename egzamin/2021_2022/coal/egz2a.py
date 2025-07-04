from egz2atesty import runtests

def coal(A, T):
    magazines = []
    thatone = 0
    for coal_amount in A:
        placed = False
        for i in range(len(magazines)):
            if magazines[i] + coal_amount <= T:
                magazines[i] += coal_amount
                placed = True
                thatone = i
                break

        if not placed:
            magazines.append(coal_amount)
            thatone = len(magazines) - 1
    return thatone

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = False )

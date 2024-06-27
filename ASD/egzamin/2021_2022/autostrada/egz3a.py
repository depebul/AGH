from egz3atesty import runtests

def snow( T, I ):
    tab = [0] * T
    for i in I:
        for j in range(i[0], i[1] + 1):
            tab[j] += 1
    return max(tab)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

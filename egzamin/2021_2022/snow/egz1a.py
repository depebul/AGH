from egz1atesty import runtests

def snow( S ):
    S.sort(reverse = True)
    i = 0
    res = 0
    while S[i] - i > 0:
        res += S[i] - i
        i += 1
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

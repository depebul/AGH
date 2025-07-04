# Dawid Żak, mój algorytm tworzy na początku dwie tablice, dla ruchu w górę i dla ruchu w dół, następnie wypełnia je
# wartościami -1, jeśli dana komnata jest niedostępna wpisuję -inf, wartość startowa to 0 dla punktu (0,0), funkcja gora()
# najpierw sprawdza czy dany ruch w górę jest możliwy, jeśli tak to sprawdza czy wartość dla danego pola jest już obliczona,
# jeśli tak to zwraca ją, jeśli nie to sprawdza czy większą wartość otrzyma z ruchu w prawo na aktualną pozycje, czy z ruchu
# w górę na aktualną pozycje, funkcja dol() działa analogicznie do funkcji gora(), funkcja prawo() zwraca maksymalną wartość
# z ruchu w dół i z ruchu w górę, zaczynam funkcję od celu w prawym dolnym rogu.

from zad7testy import runtests


def maze(L):
    n = len(L)
    dol_tab = [[-1 for _ in range(n)] for _ in range(n)]
    gora_tab = [[-1 for _ in range(n)] for _ in range(n)]
    gora_tab[0][0] = dol_tab[0][0] = 0
    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                dol_tab[i][j] = float("-inf")
                gora_tab[i][j] = float("-inf")

    def gora(y, x):
        if not (x < 0 or y < 0 or x > n or y > n or L[y][x] == '#'):
            if gora_tab[y][x] != -1:
                return gora_tab[y][x]
            gora_tab[y][x] = max(prawo(y, x - 1) + 1, gora(y - 1, x) + 1)
            return gora_tab[y][x]
        return float("-inf")

    def dol(y, x):
        if not (x < 0 or y < 0 or x >= n or y >= n or L[y][x] == '#'):
            if dol_tab[y][x] != -1:
                return dol_tab[y][x]
            dol_tab[y][x] = max(prawo(y, x - 1) + 1, dol(y + 1, x) + 1)
            return dol_tab[y][x]
        return float("-inf")

    def prawo(y, x):
        return max(dol(y, x), gora(y, x))

    ok = prawo(n - 1, n - 1)
    return ok if ok > 0 else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)

# Dawid Żak - najpierw tworzymy dwie tablice Tx i Ty, które będą przechowywały ilość punktów
# o danej współrzędnej x i y mniejszych lub równych danej współrzędnej. Następnie tworzymy tablicę T,
# która przechowuje ilość punktów zdominowanych przez ten punkt. wyliczana jest ona za pomocą wzoru który
# polega na tym iż zbiory Tx i Ty na pozycji o 1 mniejszej od naszego elementu posiadają punkty mniejsze od niego
# i po zsumowaniu tych wartości zauważamy że dwa razy zostały policzone punkty które są mniejsze od naszego punktu
# na obu pozycjach, dla punktu który nie jest dominowany otrzymujemy właściwą ilość punktów dominowanych
# przez nasz punkt po odjęciu ilości wszystkich punktów, dlatego że wszystkie punkty będą zawarte w Tx i Ty na pozycji
# o jedno mniejszej od niego i tak jak wcześniej napisałem policzyliśmy dwa razy punkty zdominowane przez niego.
# Należy dodać 1 ponieważ nasz punkt to jedyny punkt nie zawarty w Tx i Ty dla jego pozycji.
# Złożoność czasowa to O(n), złożoność pamięciowa to O(n).


from zad3testy import runtests

def dominance(P):
    Tx = [0] * (len(P) + 1)
    Ty = [0] * (len(P) + 1)
    T = [0] * len(P)
    for i in range(len(P)):
        Tx[P[i][0]] += 1
        Ty[P[i][1]] += 1
    for i in range(1, len(P) + 1, 1):
        Tx[i] += Tx[i - 1]
        Ty[i] += Ty[i - 1]
    for i in range(len(P)):
        T[i] = Tx[P[i][0] - 1] + Ty[P[i][1] - 1] - len(P) + 1
    return max(T)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

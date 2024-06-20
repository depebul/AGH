# Dawid Żak, mój algorytm działa na zasadzie sprawdzania ile należy wyciąć drzew aby uzyskać każdą
# możliwą resztę z dzielenia przez m idąc po sumie "i" tych drzew, startujemy, w pętli po m
# sprawdzamy najpierw jaka jest reszta po dodaniu nowego drzewa i następnie porównujemy czy
# bardziej nam się opłaca wyciąć kolejne drzewo dla nowej reszty, czy już zdarzyło nam się
# policzyć to lepiej i tak to zostawiamy. złożoność czasowa to O(n^2).


from kol3testy import runtests


def orchard(T, m):
    n = len(T)
    reszta = sum(T) % m
    tab = [float('inf')] * m
    tab[0] = 0
    for i in range(n):
        new_tab = tab[:]
        for j in range(m):
            new_reszta = (j + T[i]) % m
            new_tab[new_reszta] = min(new_tab[new_reszta], tab[j] + 1)
        tab = new_tab
    return tab[reszta]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
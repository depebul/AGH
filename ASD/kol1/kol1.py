# Dawid Żak, do mojego algorytmu wykorzystałem analogiczny sposób co w zadaniu offline 3, czyli zauważyłem, że
# jeżeli zsumujemy wszystkie elementy o mniejszym indexie niż nasz punkt z elementami które są od niego mniejsze
# to dla elementu o największej randze zsumujemy wszystkie punkty, lecz dwa razy dodamy elementy które są od
# niego mniejsze indeksem i wartością, czyli po odjęciu ilości wszystkich punktów mamy właściwą range, trzeba rzecz
# jasna jeszcze dodać 1 punkt, czyli ten sprawdzany. do sortowania wykorzystałem quicksorta.
# Ten algorytm ma złożoność obliczeniową O(nlogn) i złożoność pamięciową O(n).

from kol1testy import runtests


def quicksort(T):
    if len(T) <= 1:
        return T
    else:
        pivot = T[0]
        less_than_pivot = [x for x in T[1:] if x[0] <= pivot[0]]
        greater_than_pivot = [x for x in T[1:] if x[0] > pivot[0]]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def maxrank(T):
    newlist = []
    for i in range(len(T)):
        newlist.append((T[i], i))
    Ti = quicksort(newlist)
    orderlist = [0]*(len(T) + 1 )
    for i in range(len(T)):
        orderlist[Ti[i][1]] = i
    tab = [0]*len(T)
    for i in range(len(T)):
        tab[i] = orderlist[i] + i - len(T) + 1
    return max(tab)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )

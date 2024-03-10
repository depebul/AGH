from zad1testy import Node, runtests
# Dawid Żak, do tego zadania wykorzystałem algorytm sortujący selection sort
# ponieważ jest to lista jednokierunkowa, zdecydowałem się na zamianę wartości
# w polu value między "Node"ami, obiekt Node uznaję analogicznie do zwykłego algorytmu
# jako jedynie miejscę na wartość, pierwsza pętla zależna od zmiennej p służy za ogólne poruszanie
# się po liście, pętla zależna od zmiennej jumper polega na znajdywaniu w odległości conajwyżej k
# najmniejszej wartości aby zamienić jej wartość z polem p.val



def SortH(p,k):
    start = p
    while p is not None:
        changer = None
        minf = float("inf")
        jumper = p
        jumps = 0
        while jumper is not None and jumps <= k:
            if jumper.val < minf:
                minf = jumper.val
                changer = jumper
            jumper = jumper.next
            jumps += 1
        changer.val, p.val = p.val, changer.val
        p = p.next
    return start


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )

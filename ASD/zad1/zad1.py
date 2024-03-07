from zad1testy import Node, runtests


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

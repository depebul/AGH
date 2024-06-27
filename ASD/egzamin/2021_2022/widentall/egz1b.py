from egz1btesty import runtests
from math import inf


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = None  # pole do wykorzystania przez studentow


def wideentall(T):
    sum_tab = [[T]]

    T.x = [0,None,False]#rzad, parent, lucky
    great_sum = 0

    def jazda(T):
        if T.left:
            new_left_rzad = T.x[0] + 1
            if len(sum_tab) <= new_left_rzad:
                sum_tab.extend([[]] * (new_left_rzad - len(sum_tab) + 1))
            T.left.x = [new_left_rzad, T, False]
            sum_tab[new_left_rzad].append(T.left)
            jazda(T.left)
        if T.right:
            new_right_rzad = T.x[0] + 1
            if len(sum_tab) <= new_right_rzad:
                sum_tab.extend([[]] * (new_right_rzad - len(sum_tab) + 1))
            T.right.x = [new_right_rzad, T, False]
            sum_tab[new_right_rzad].append(T.right)
            jazda(T.right)

    def lezgo(T):
        if T.x[2] == True:
            return
        T.x[2] = True
        if T.x[1] is not None:
            lezgo(T.x[1])

    def sprawdzamy(T):
        nonlocal great_sum
        if T.left is not None:
            if T.left.x[2]:
                sprawdzamy(T.left)
            else:
                great_sum += 1
        if T.right is not None:
            if T.right.x[2]:
                sprawdzamy(T.right)
            else:
                great_sum += 1

    jazda(T)
    max = -inf
    ind = 0
    for i in range(len(sum_tab)):
        if len(sum_tab[i]) >= max:
            max = len(sum_tab[i])
            ind = i
    for el in sum_tab[ind]:
        lezgo(el)
    sprawdzamy(T)
    return great_sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )

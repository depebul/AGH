# Dawid Żak mój algorytm polega na tym iż na początku tworzy posortowaną tablicę p elementową przy pomocy
# quick sorta, podczas następnych pętli usuwa element który znajdował się w poprzednim zakresie p i dodaje następny
# element, który ma znaleźć się w zakresie p, wykorzystuje do jego znalezienia algorytm binary search, do usunięcia
# elementu z templist stosuje funkcję del i do wstawienia używa insert. Algorytm ten posiada złożoność czasową O(np)
# i złożoność pamięciową O(p)


from zad2testy import runtests

def ksum(T, k, p):
    n = len(T)
    templist = makelist(T,p)
    sum = templist[p - k]
    i = 0
    while i + p < n:
        templist = changelist(T,i,templist,p)
        i += 1
        sum += templist[p - k]
    return(sum)

def changelist(T, i, templist, p):
    the_ind = binary_search(templist, T[i])
    del templist[the_ind]
    templist.insert(binary_search(templist, T[p + i]), T[p + i])
    return templist

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def makelist(T,p):
    i = 0
    templist = []
    while i < p:
        templist.append(T[i])
        i += 1
    return quick_sort(templist)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )

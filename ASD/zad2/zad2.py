from zad2testy import runtests

def ksum(T, k, p):
    n = len(T)
    ind = 0
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

def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
    for j in range(l , h):
        if arr[j] <= x:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

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

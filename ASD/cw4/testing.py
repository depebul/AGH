
def binary_search(T: list,k : int):
    left = 0
    right = len(T) - 1
    while left <= right:
        mid = (left + right) // 2
        if T[mid] == k:
            return mid
        elif T[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1


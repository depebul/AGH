
def colors(T,k):
    n = len(T)
    start = 0
    min_len = float('inf')
    distinct_count = 0
    count = [0]*k
    min_start, min_end = -1, -1
    for i in range(n):
        count[T[i]] += 1
        if count[T[i]] == 1:
            distinct_count += 1
        while distinct_count == k:
            if i - start + 1 < min_len:
                min_len = i - start + 1
                min_start, min_end = start, i
            count[T[start]] -= 1
            if count[T[start]] == 0:
                distinct_count -= 1
            start += 1
    return (min_start, min_end) if min_len != float('inf') else (-1, -1)

T=[0,2,1,0,2,2,0,2,3,3,2,1,0,3]
print(colors(T,4))
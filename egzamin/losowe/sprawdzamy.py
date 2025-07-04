def sort_key(x):
    return x[0], x[1]

def uncool( P ):
    n = len(P)

    L = []
    for i in range(n):
        L.append([P[i][0], P[i][1], i])
    L.sort(key=sort_key)


    start = L[0][0]
    end = L[0][1]
    index = 0
    for i in range(1, n):
        A = L[index]
        B = L[i]
        cool = False

        if (A[0] >= B[0] and A[1] <= B[1]) or (B[0] >= A[0] and B[1] <= A[1]):
            cool = True
        elif (A[1] < B[0]) or (A[0] > B[1]):
            cool = True

        if not cool:
            return (A[2], B[2])
        else:
            if B[1] - B[0] >= end - start:
                end = B[1]
                start = B[0]
                index = i

    for i in range(n - 1):
        A = L[i]
        B = L[i + 1]
        cool = False

        if (A[0] >= B[0] and A[1] <= B[1]) or (B[0] >= A[0] and B[1] <= A[1]):
            cool = True
        elif (A[1] < B[0]) or (A[0] > B[1]):
            cool = True

        if not cool:
            return (A[2], B[2])



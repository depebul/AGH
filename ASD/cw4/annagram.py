
def annagram(A,B,k):
    arr = [0]*26
    for i in range(k):
        arr[ord(A[i])-97] += 1
        arr[ord(B[i])-97] -= 1
    for i in arr:
        if i != 0:
            return False
    return True

print(annagram("bruhman","manbruh",7))
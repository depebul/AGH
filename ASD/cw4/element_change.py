
def element_change(T,k):
    T[:k] = T[:k][::-1]
    T[k:] = T[k:][::-1]
    T.reverse()
    return T
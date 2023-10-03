def KMP(T, n, P, m):
    next = computa_next(P, m)
    i = 0
    j = 0
    index = -1
    while index == -1 and i < n:
        if P[j] == T[i]:
            j += 1
            i += 1
        else:
            j = next[j]
            if j == -1:
                j = 0
                i += 1
        if j == m:
            index = i-m
    return index

def computa_next(P, m):
    next = [0]*m
    next[0] = -1
    next[1] = 0
    for i in range(2,m):
        j = next[i-1] + 1
        while P[i-1] != P[j] and j > 0:
            j = next[j] +1
        next[i] = j
    return next

P = "arara"
m = len(P)
T = "rapaz que arara braba"
n = len(T)

print(KMP(T, n, P, m))
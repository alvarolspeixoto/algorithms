def merge_sort(X, n):
    return merge(X, 0, n-1)

def merge(X, esq, dir):
    if esq < dir:
        meio = (dir + esq) // 2
        merge(X, esq, meio)
        merge(X, meio+1, dir)
        aux(X, esq, meio, dir)

def aux(Y, le, m, r):
    tamA = m-le+1
    tamB = r - m
    A = [0]*tamA
    B = [0]*tamB
    
    for i in range(0,tamA):
        A[i] = Y[le + i]
    for j in range(0,tamB):
        B[j] = Y[j + m + 1]
    
    i = 0
    j = 0
    k = le

    while i < tamA and j < tamB:
        if A[i] <= B[j]:
            Y[k] = A[i]
            i += 1
        else:
            Y[k] = B[j]
            j += 1
        k += 1

    while i < tamA:
        Y[k] = A[i]
        i += 1
        k += 1
    while j < tamB:
        Y[k] = B[j]
        j += 1
        k += 1



    
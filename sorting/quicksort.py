def quicksort(X, n):
    qsort(X, 0, n-1)

def qsort(X, esq, dir):
    
    if esq < dir:
        pos = particao(X, esq, dir)
        qsort(X, esq, pos-1)
        qsort(X, pos+1, dir)

def particao(X, esq, dir):
    pivo = X[esq]
    L = esq
    R = dir
    while L < R:
        while X[L] <= pivo and L < dir:
            L += 1
        while X[R] > pivo and R > esq:
            R -= 1
        if L < R:
            X[L], X[R] = X[R], X[L]
    pos = R
    X[esq], X[pos] = X[pos], X[esq]
    return pos

X = [4,6,4,1,-1,0,10,9,56,3]
n = len(X)
quicksort(X, n)
print(X)

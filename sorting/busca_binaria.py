def aux(A, esquerda, direita, item):
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    if A[meio] == item:
        return meio
    elif A[meio] > item:
        return aux(A, esquerda, meio - 1, item)
    else:
        return aux(A, meio + 1, direita, item)

def busca_binaria(A, x):
    n = len(A)
    return aux(A, 0, n-1, x)
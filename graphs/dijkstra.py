from math import inf

def montaMinHeap(A, D, n):
    for i in range(n//2-1,-1,-1):
        minHeapify(A, D, i, n)

def minHeapify(A, D, i, n):
    esq = 2*i + 1
    dir = 2*i + 2
    if esq < n and D[A[esq]] < D[A[i]]:
        menor = esq
    else:
        menor = i
    if dir < n and D[A[dir]] < D[A[menor]]:
        menor = dir
    if menor != i:
        A[i], A[menor] = A[menor], A[i]
        minHeapify(A, D, menor, n)

def removeMinHeap(A, D, n):
    if n == 0:
        return 
    else:
        x = A[0]
        A[0] = A[n-1]
        n -= 1
        A.pop()
        minHeapify(A, D, 0, n)
    return x


def dijkstra(G, s):
    if len(G) == 1:
        return 0
    S = []
    n = len(G)
    D = [inf]*(n+1)
    D[s] = 0
    Q = [x for x in range(1, n+1)]
    print(Q)
    montaMinHeap(Q, D, n)
    print(Q)

    while Q:
        v = removeMinHeap(Q, D, n)
        n -= 1
        S.append(v)
        pesos = G[v-1]
        k = len(pesos)
        for i in range(1,k+1):
                D[i] = min(D[i], D[v] + pesos[i-1])
                minHeapify(Q, D, i-1, n)
                # montaMinHeap(Q, D, n)
    return D[1:]

# Teste
m1 = [[0, 10, 3, 0, 0],
      [0, 0, 1, 2, 0],
      [0, 4, 0, 8, 2],
      [0, 0, 0, 0, 9],
      [0, 0, 0, 7, 0]]

m2 = [0]

m3 = [[0, 3, 1],
      [6, 0, 400],
      [2, 4, 0]]

m4 = [[0, 57148, 51001, 13357],
    [71125, 0, 98369, 67226],
    [49388, 90852, 0, 66291],
    [39573, 38165, 97007, 0]]

# print(dijkstra(m4, 4))

M = """ 
0 74961 47889 4733 72876 21399 63105 48239
15623 0 9680 89133 57989 63401 26001 29608
42369 82390 0 32866 46171 11871 67489 54070
23425 80027 18270 0 28105 42657 40876 29267
78793 18701 7655 94798 0 88885 71424 86914
44835 76636 11553 46031 13617 0 16971 51915
33037 53719 43116 52806 56897 71241 0 11629
2119 62373 93265 69513 5770 90751 36619 0
 """
G = []
for _ in range(8):
    line = [int(x) for x in input().split()]
    G.append(line)

# dij = dijkstra(G, 8)
# print(sum(dij))

n = len(m4)
soma = 0
for i in range(1, 9):
    dij = dijkstra(G, i)
    print(*dij)
    soma += sum(dij)

print(soma)



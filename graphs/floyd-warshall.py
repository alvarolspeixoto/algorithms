from math import inf

def read_matrix(n):
    M = []
    for _ in range(n):
        M.append([int(x) for x in input().split()])
    return M

def sum_all(M):
    total = 0
    for row in M:
        total += sum(row)
    return total

def floyd_warshall(D):
    n = len(D)
    L = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if D[i][j] == 0 and i != j:
                L[i][j] = inf
            else:
                L[i][j] = D[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                L[i][j] = min(L[i][j], L[i][k] + L[k][j])
    rows_sum = sum_all(L)
    return rows_sum

n = int(input())
G = read_matrix(n)
vertices = [int(x) - 1 for x in input().split()]

for i in range(n):
    v = vertices[i]
    print(floyd_warshall(G))
    del G[v]
    for row in G:
        del row[v]
    for j in range(i+1, n):
        if vertices[i] < vertices[j]:
            vertices[j] -= 1
def computa_deslocamento(P, m):
    tabela = {}
    for i in range(m-1):
        tabela[P[i]] = m - 1 - i
    return tabela

def hoorspool(T, n, P, m):
    tabela = computa_deslocamento(P, m)
    i = m-1
    ocorrencias = []
    while i < n:
        k = 0
        while k < m and P[m-1-k] == T[i-k]:
            k += 1
        if k == m:
            ocorrencias.append(i-m+1)
        i += tabela.get(T[i], m)
    return ocorrencias

P = "deveria"
m = len(P)

T = "tu nao deveria ter pego 7, deveria Alvaro materias, deveria"
n = len(T)

# print(computa_deslocamento(P, m))

print(hoorspool(T, n, P, m))

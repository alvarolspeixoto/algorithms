class Item:
    def __init__(self) -> None:
        self.tam = None
        self.dir = None

    def __repr__(self) -> str:
        return f"({self.tam}, {self.dir})"

    def __str__(self) -> str:
        return self.__repr__()

def longa_subseq_comum(X, m, Y, n, LCS):
    # Casos base: uma das sequências é vazia
    for i in range(m+1):
        LCS[i][0].tam = 0
        LCS[i][0].dir = '*'
    for j in range(n+1):
        LCS[0][j].tam = 0
        LCS[0][j].dir = '*'
    # Caso geral
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                LCS[i][j].tam = 1 + LCS[i-1][j-1].tam
                LCS[i][j].dir = 'D'
            else:
                if LCS[i-1][j].tam > LCS[i][j-1].tam:
                    LCS[i][j].tam = LCS[i-1][j].tam
                    LCS[i][j].dir = 'A'
                else:
                    LCS[i][j].tam = LCS[i][j-1].tam
                    LCS[i][j].dir = 'E'
    return LCS

X = "abcda"
m = len(X)
Y = "bcdb"
n = len(Y)
LCS = []
for i in range(m+1):
    linha = []
    for j in range(n+1):
        linha.append(Item())
    LCS.append(linha)

LCS = longa_subseq_comum(X, m, Y, n, LCS)

def imprime_LCS(LCS, i, j, X):
    if not(i == 0 or j == 0):
        if LCS[i][j].dir == 'D':
            imprime_LCS(LCS, i-1, j-1, X)
            print(X[i-1], end='')
        else:
            if LCS[i][j].dir == 'A':
                imprime_LCS(LCS, i-1, j, X)
            else:
                imprime_LCS(LCS, i, j-1, X)

imprime_LCS(LCS, m, n, X)

    
class Object:
    def __init__(self, valor, peso) -> None:
        self.valor = valor
        self.peso = peso

    def __repr__(self) -> str:
        return f"(Valor: {self.valor}, Peso: {self.peso})"
    
    def __str__(self) -> str:
        return self.__repr__()

def knapsack(objs, n, m):
    
    V = [[0]*(m+1) for _ in range(n+1)] # Matriz n x m inicializada com 0s
    for i in range(1,n+1):
        for j in range(1, m+1):
            if objs[i-1].peso <= j:
                V[i][j] = max(V[i-1][j], V[i-1][j-objs[i-1].peso] + objs[i-1].valor)
            else:
                V[i][j] = V[i-1][j]
    i = n
    j = m
    selecionados = []
    while i > 0 and j > 0:
        if V[i][j] != V[i-1][j]:
            selecionados.append(objs[i-1])
            i -= 1
            j -= objs[i-1].peso
        i -= 1
    return selecionados


objetos = []
objetos.append(Object(1,2))
objetos.append(Object(2,3))
objetos.append(Object(5,4))
objetos.append(Object(6,5))
n = len(objetos)

res = knapsack(objetos, n, 8)
print(res)
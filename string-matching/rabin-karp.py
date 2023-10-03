def rabin_karp(T, n, P, m):
    q = 3354393
    d = 32
    dM = 1
    for i in range(m-1):
        dM = (d*dM) % q
    h1 = 0
    for i in range(m):
        h1 = (h1*d + ord(P[i])) % q
    h2 = 0
    for i in range(m):
        h2 = (h2*d + ord(T[i])) % q
    i = 0
    while h1 != h2 and i < n-m:
        h2 = (h2 + d*q - ord(T[i])*dM) % q
        h2 = (h2*d + ord(T[i+m])) % q
        i += 1
    return i


T = "muito brabo esse algoritmo"
n = len(T)
P = "algoritmo"
m = len(P)

print(rabin_karp(T, n, P, m))

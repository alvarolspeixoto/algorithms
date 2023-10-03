seq = [-1, 3, 4, 5, 2, 2, 2, 2]
n = len(seq)

def LIS(seq, n):
    LIS = [1]*n
    for i in range(n):
        for j in range(i+1, n):
            if seq[i] <= seq[j]:
                LIS[j] = max(LIS[j], 1 + LIS[i])

    return LIS

# print(LIS(seq, n))
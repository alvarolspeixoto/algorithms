# Checa se um array é um max heap
def solve(nums):
   n = len(nums)
   for i in range(n):
      m = i * 2
      num = nums[i]
      if m + 1 < n:
         if num < nums[m + 1]:
            return False
      if m + 2 < n:
         if num < nums[m + 2]:
            return False
   return True

# funções para manipular max heap
def MontaMaxHeap(A, n):
    for i in range(n//2-1,-1,-1):
        MaxHeapify(A,i,n)
    

def MaxHeapify(A, i, n):
    esq = 2*i + 1
    dir = 2*i + 2
    if esq < n and A[esq] > A[i]:
        maior = esq
    else:
        maior = i
    if dir < n and A[dir] > A[maior]:
        maior = dir
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        MaxHeapify(A, maior, n)

def InsereMaxHeap(A, n, x):
    A.append(x)
    n += 1
    filho = n - 1
    pai = (n - 1) // 2
    while pai >= 0:
        if A[pai] < A[filho]:
            A[pai], A[filho] = A[filho], A[pai]
            filho = pai
            pai = (pai-1) // 2 
        else:
            pai = -1

def removeMaxHeap(A, n):
    if n == 0:
        return
    else:
        x = A[0]
        A[0] = A[n-1]
        n -= 1
        MaxHeapify(A,0,n)
    return x

def heapsort(A, n):
    MontaMaxHeap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MaxHeapify(A, 0, i)
   


""" A = [6, 7, 8, 2]
n = len(A)
MontaMaxHeap(A, n)
print(A)
print(solve(A))
heapsort(A, n)
print(A)
 """

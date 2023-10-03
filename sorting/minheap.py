""" def solve(nums):
   n = len(nums)
   for i in range(n):
      m = i * 2
      num = nums[i]
      if m + 1 < n:
         if num > nums[m + 1]:
            return False
      if m + 2 < n:
         if num > nums[m + 2]:
            return False
   return True """

def montaMinHeap(A, n):
    for i in range(n//2-1,-1,-1):
        minHeapify(A,i,n)

def minHeapify(A, i, n):
    esq = 2*i + 1
    dir = 2*i + 2
    if esq < n and A[esq] < A[i]:
        menor = esq
    else:
        menor = i
    if dir < n and A[dir] < A[menor]:
        menor = dir
    if menor != i:
        A[i], A[menor] = A[menor], A[i]
        minHeapify(A, menor, n)

def insereMinHeap(A, n, x):
    A.append(x)
    n += 1
    filho = n - 1
    pai = (n - 1) // 2
    while pai >= 0:
        if A[pai] > A[filho]:
            A[pai], A[filho] = A[filho], A[pai]
            filho = pai
            pai = (pai-1) // 2 
        else:
            pai = -1

def removeMinHeap(A, n):
    if n == 0:
        return 
    else:
        x = A[0]
        A[0] = A[n-1]
        n -= 1
        # A.pop()
        minHeapify(A,0,n)
    return x

""" A = [(10,0,0),(8,0,0),(11,0,0),(12,0,0),(5,0,0),(3,0,0)]
n = len(A)
montaMinHeap(A, n)
print(A)
print(solve(A)) """
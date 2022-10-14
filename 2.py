N = int(input("Введите размер массива A: ")) 
A = [0] * N
N2 = int(input("Введите размер массива B: ")) 
B = [0] * N2
from random import uniform 
for i in range(N): 
        A[i] = uniform(0.0,3.0)
        A[i] = round(A[i], 1)# или A[i] = float(input("Заполните массив: "))
A = list(set(A))
for i in range(N2): 
        B[i] = uniform(0.0,3.0)
        B[i] = round(B[i], 1)
B = list(set(B))
A_B = []
for a in A:
    if a in B:
        A_B.append(a)
print (A_B)        

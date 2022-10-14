N = int(input("Введите размер массива: "))
A = [0] * N
from random import uniform
for i in range(N):
        A[i] = uniform(-99.0,99.0) # или A[i] = float(input("Заполните массив: "))
print ("Входной массив:", A)
max_A = max(A)
for i in range(A.index(max_A)+1, N):
        A[i] = 0
print ("Результат:", A)

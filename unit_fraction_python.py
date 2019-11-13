import sys
import math

# https://math.stackexchange.com/questions/921456/how-do-i-prove-that-any-unit-fraction-can-be-represented-as-the-sum-of-two-other
# Utilizando a decomposição:
#
# 1/n = k / n(n+k) + 1 / (n+k), 
#
# onde max(k) == n e n(n + k) / k é inteiro positivo

# Determinar o max(k) foi muito importante para limitar o número de iterações

n = int(input())

for k in range(1, n + 1):
    x = n * (n + k) / k
    
    if x.is_integer():
        x = int(x)
        print(f"1/{n} = 1/{x} + 1/{n + k}")

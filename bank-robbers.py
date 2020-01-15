import sys
import math

r = int(input())
v = int(input())

vaults = []
for i in range(v):
    c, n = [int(j) for j in input().split()]
    
    vowels_counter = c - n
    time_to_robber = pow(10, n) * pow(5, vowels_counter)
    vaults.append(time_to_robber)
    
robbers_time = [0 for i in range(r)]
while len(vaults) > 0:
    index = robbers_time.index(min(robbers_time))
    robbers_time[index] += vaults[0]
    vaults.pop(0)

print(max(robbers_time))

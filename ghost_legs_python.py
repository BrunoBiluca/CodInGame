import sys
import math


w, h = [int(i) for i in input().split()]
diagram = []
for i in range(h):
    line = input()
    diagram.append(line)
    

result = []
for t in diagram[0]:
    if t == " ":
        continue
    
    x = diagram[0].index(t)
    for line in diagram[1:-1]:
        x_turn_left = x - 3
        left_bound = x_turn_left if x_turn_left >= 0 else 0
        
        x_turn_right = x + 3
        right_bound = x_turn_right if x_turn_right < w else w
        i = line.find("--", left_bound, right_bound)
        
        if i == -1:
            continue
        
        x = x_turn_right if x < i else x_turn_left

    b = diagram[-1][x]
    result.append(f"{t}{b}")

for r in result:
    print(r)

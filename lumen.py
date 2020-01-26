import sys
import math

n = int(input())
l = int(input())

room_map = {f"{i}_{j}": "X" for i in range(n) for j in range(n)}
dark_spots = pow(n, 2)

for i in range(n):
    line = input()
    
    line_candles = [pos for pos, value in enumerate(line.split(' ')) if value == "C"]
    light_range = l - 1
    for j in line_candles:
        left = i - light_range
        right = i + light_range
        top =  j - light_range
        bottom = j + light_range 
        
        for y in range(left, right + 1):
            for x in range(top, bottom + 1):
                try:
                    if room_map[f"{y}_{x}"] == "X":
                        dark_spots += -1
                    room_map[f"{y}_{x}"] = "L"
                except KeyError:
                    continue

print(dark_spots)

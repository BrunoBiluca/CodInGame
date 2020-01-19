import sys
import math

n = int(input())
l = int(input())

candles = {}
for i in range(n):
    line = input()
    line_candles = [pos for pos, value in enumerate(line.split(' ')) if value == "C"]

    for j in line_candles:
        candles[f"{i}_{j}"] = {
            "left": i - l if i - l > 0 else 0,
            "right": i + l if i < n else n - 1,
            "top": j - l if j - l > 0 else 0,
            "bottom": j + l if j + l < n else n - 1
        }
    
candles_iluminate_area = 0
intersection_area = 0
for key, candle in candles.items():
    candles_iluminate_area += (candle["right"] - candle["left"]) * (candle["bottom"] - candle["top"])
    # print(key, candles_iluminate_area)
    for second_key, second_candle in candles.items():
        if key == second_key:
            continue
        
        overlay_x = min(candle["right"], second_candle["right"]) - max(candle["left"], second_candle["left"])
        overlay_y = min(candle["bottom"], second_candle["bottom"]) - max(candle["top"], second_candle["top"])
        intersection_area += overlay_x * overlay_y

result = pow(n, 2) - candles_iluminate_area - intersection_area

print(result)

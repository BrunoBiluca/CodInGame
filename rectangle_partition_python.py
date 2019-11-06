import sys
import math


def build_measurements(points):
    measurements = {}
    measurements_intervals = []
    
    for i in points:
        position = int(i)
        for interval in measurements_intervals:
            count_value_in_rectangle(position - interval, measurements)
    
        count_value_in_rectangle(position, measurements)
        measurements_intervals.append(position)
        
    return measurements


def count_value_in_rectangle(key, measurements):
    measurements[key] = measurements[key] + 1 if key in measurements else 1


w, h, count_x, count_y = [int(i) for i in input().split()]

x_values = input().split()
x_values.append(w)
measurements_x = build_measurements(x_values)

y_values = input().split()
y_values.append(h)
measurements_y = build_measurements(y_values)

count_squares = 0
for key, value in measurements_x.items():
    count_squares = count_squares + (value * measurements_y.get(key, 0))
        
print(count_squares)

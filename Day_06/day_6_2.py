#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
import re
import numpy as np
input = open("input.txt", "r")
data = input.readlines()

times = re.findall('[0-9]+', data[0])
distances = re.findall('[0-9]+', data[1])

times = int(''.join(time for time in times))
distances = int(''.join(distance for distance in distances))

coeffs = [-1, times, -distances] #based on derived quadratic formula for distance over charge time
roots = np.roots(coeffs)
roots[1] = np.ceil(roots[1])
roots[0] = np.floor(roots[0])
print(f"{(roots[0]-roots[1]+1):.0f}")
#answer is 23654842
#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
import re
input = open("input.txt", "r")
data = input.readlines()

times = re.findall('[0-9]+', data[0])
distances = re.findall('[0-9]+', data[1])
ways = [0] * len(times)
speed = 0
distance = 0
result = 1

for race_no, time in enumerate(times):
    for charge_time in range(0,int(time)+1):
        speed = charge_time
        distance = (int(time) - charge_time) * speed
        if distance > int(distances[race_no]):
            ways[race_no] += 1
for way in ways:
    result *= way
print(result)
#answer is 303600
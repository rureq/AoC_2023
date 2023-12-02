#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()

max_red = 12
max_green = 13
max_blue = 14
sum = 0
reds, greens, blues = [], [], []

for line_no, line in enumerate(data):
    stripped_line = line.split(": ")[1]
    sets = stripped_line.split("; ")
    for set in sets:
        cubes = set.split(", ")
        for cube in cubes:
            colors = cube.split(" ")
            num = int(colors[0])
            if colors[1][0] == 'r':
                reds.append(num)
            elif colors[1][0]  == 'g':
                greens.append(num)
            elif colors[1][0]  == 'b':
                blues.append(num)
    
    sum += max(reds) * max(greens) * max(blues)
    
    reds, greens, blues = [], [], []

print(sum)
#69629
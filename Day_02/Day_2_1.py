#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()

max_red = 12
max_green = 13
max_blue = 14
sum = 0
check = 0

for line_no, line in enumerate(data):
    stripped_line = line.split(": ")[1]
    sets = stripped_line.split("; ")
    for set in sets:
        cubes = set.split(", ")
        for cube in cubes:
            colors = cube.split(" ")
            num = int(colors[0])
            if colors[1][0] == 'r':
                if num > max_red:
                    check += 1
            elif colors[1][0]  == 'g':
                if num > max_green:
                    check += 1
            elif colors[1][0]  == 'b':
                if num > max_blue:
                    check += 1
    if check == 0:
        sum += line_no + 1
    check = 0
print(sum)
#2632
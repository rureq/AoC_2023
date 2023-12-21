#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()
result = 0

class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = 0
    y = 0

galaxies = []
rows = []
cols = []

i = 0
while i != len(data):
    data[i] = data[i].replace('\n', '')
    if data[i].count('.') == len(data[i]):
        rows.append(1)
    else:
        rows.append(0)
    i+=1

k = 0
while k != len(data[0]):
    spaces = 0
    for line in data:
        if line[k] == '.':
            spaces += 1
    if spaces == len(data):
        cols.append(1)
    else:
        cols.append(0)
    k += 1
    
for y, line in enumerate(data):
    for x, place in enumerate(line):
        if place == '#':
            galaxies.append(Galaxy(x,y))
            
for i, galaxy in enumerate(galaxies):
    for gx in galaxies[i+1:]:
        indices = [galaxy.x, gx.x]
        indices.sort()
        result += abs(gx.x - galaxy.x) + abs(gx.y - galaxy.y) + cols[indices[0]:indices[1]+1].count(1)*999999 + rows[galaxy.y:gx.y+1].count(1)*999999
print(result)
#answer is 447744640566
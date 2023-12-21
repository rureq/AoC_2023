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

i = 0
while i != len(data):
    data[i] = data[i].replace('\n', '')
    if data[i].count('.') == len(data[i]):
        data.insert(i,len(data[i])*'.')
        i+=1
    i+=1

k = 0
while k != len(data[0]):
    spaces = 0
    for line in data:
        if line[k] == '.':
            spaces += 1
    if spaces == len(data):
        for j,l in enumerate(data):
            nl = list(data[j])
            nl.insert(k,'.')
            data[j] = ''.join(nl)
        k += 1
    k += 1

for y, line in enumerate(data):
    for x, place in enumerate(line):
        if place == '#':
            galaxies.append(Galaxy(x,y))
            
for i, galaxy in enumerate(galaxies):
    for gx in galaxies[i:]:
        result += abs(gx.x - galaxy.x) + abs(gx.y - galaxy.y)
print(result)
#answer is 9536038
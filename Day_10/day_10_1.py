#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()

class Node:
    def __init__(self, kind):
        self.kind = kind
        if kind == "L":
            self.dirs = [1,2]
        elif kind == 'F':
            self.dirs = [2,-1]
        elif kind == '7':
            self.dirs = [-1,-2]
        elif kind == 'J':
            self.dirs = [-2,1]
        elif kind == '|':
            self.dirs = [1,-1]
        elif kind == '-':
            self.dirs = [2,-2]
        elif kind == 'S':
            self.dirs = [1,2,-1,-2]
        else:
            pass

    def __str__(self):
        return self.kind

    dirs = []
    kind = ''
    distance = 0

grid = []
x,y = 0,0

for line in data:
    line = line.replace('\n', '')
    grid.append([Node(x) for x in line])

x_start = -1
y_start = -1
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y].kind == 'S':
            x_start = x
            y_start = y
            break
    if x_start != -1:
        break   

dist = 0
dir = -1
x_next = x_start
y_next = y_start
grid[x_start][y_start].distance = -1

while True:
    dist += 1
    if dir == -1:
        x_next += 1
    elif dir == 1:
        x_next -= 1
    elif dir == 2:
        y_next += 1
    elif dir == -2:
        y_next -= 1
    if dir * -1 in grid[x_next][y_next].dirs:
        if grid[x_next][y_next].distance == 0:
            grid[x_next][y_next].distance = dist
            new_dir = grid[x_next][y_next].dirs.copy()
            new_dir.pop(new_dir.index(-1*dir))
            dir = new_dir[0]
        else:
            break
print(f"{(dist/2):.0f}")
#answer is 6714
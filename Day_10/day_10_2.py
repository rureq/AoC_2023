#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
import numpy as np
input = open("input.txt", "r")
data = input.readlines()

class Node:
    def __init__(self, kind):
        self.kind = kind
        self.norm = np.array([0,0,0])
        if kind == "L":
            self.dirs = [1,2]
            self.vecs = [np.array([1,1,0]), np.array([-1,-1,0])]
        elif kind == 'F':
            self.dirs = [2,-1]
            self.vecs = [np.array([-1,1,0]), np.array([1,-1,0])]
        elif kind == '7':
            self.dirs = [-1,-2]
            self.vecs = [np.array([-1,-1,0]), np.array([1,1,0])]
        elif kind == 'J':
            self.dirs = [-2,1]
            self.vecs = [np.array([1,-1,0]),np.array([-1,1,0])]
        elif kind == '|':
            self.dirs = [1,-1]
            self.vecs = [np.array([0,1,0]),np.array([0,-1,0])]
        elif kind == '-':
            self.dirs = [2,-2]
            self.vecs = [np.array([-1,0,0]),np.array([1,0,0])]
        elif kind == 'S':
            self.dirs = [1,2,-1,-2]
        else:
            pass

    def __str__(self):
        return self.kind

    dirs = []
    vecs = []
    norm = np.array([0,0,0])
    kind = ''
    distance = 0
    visited = 0

grid = []

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
    
side = 1 #choose which side of the pipeline should be taken into consideration 
if side == 1:
    k = np.array([0,0,1])
elif side == -1:
    k = np.array([0,0,-1])
    
dist = 0
dir = -1
x_next = x_start
y_next = y_start
grid[x_start][y_start].distance = -1
grid[x_start][y_start].visited = 1
norm = [-1,0]

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
            grid[x_next][y_next].visited = 1
            new_dir = grid[x_next][y_next].dirs.copy()
            vec = grid[x_next][y_next].vecs[grid[x_next][y_next].dirs.index(-1*dir)]
            norm = np.cross(k, vec)
            grid[x_next][y_next].norm = norm
            new_dir.pop(new_dir.index(-1*dir))
            dir = new_dir[0]
        else:
            break

counter = 0
direction = 0
#prints in the loop below show directions of normal vectors
for x in grid:
    for nd in x:
        if nd.kind == 'S':
            print('s', end ='')
        else:
            if (nd.norm == np.array([-1,0,0])).all() or (nd.norm == np.array([1,0,0])).all():
                print('-', end = '')
            elif (nd.norm == np.array([0,-1,0])).all() or (nd.norm == np.array([0,1,0])).all():
                print('|', end = '')
            elif (nd.norm == np.array([-1,-1,0])).all() or (nd.norm == np.array([1,1,0])).all():
                print('\\', end = '')
            elif (nd.norm == np.array([1,-1,0])).all() or (nd.norm == np.array([-1,1,0])).all():
                print('/', end = '')
            else:
                print('.',end = '')
        if nd.visited == 1:
            direction = nd.norm[0]
        elif nd.visited == 0  and direction > 0:
            counter += 1
print()
print(counter)
#answer is 429
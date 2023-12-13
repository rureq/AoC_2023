#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()

history = []
i = 0
result = 0

for line in data:
    history.append([])
    k = 0
    history[i].append([int(x) for x in line.split()])
    while not all(y == 0 for y in history[i][k]):
        history[i].append([history[i][k][j+1] - history[i][k][j] for j, member in enumerate(history[i][k][:-1])])
        k += 1
    history[i][-1].append(0)
    history[i].reverse()
    for l, set in enumerate(history[i][1:]):
        set.append(history[i][l][-1] + set[-1])
    result += history[i][-1][-1]
    i += 1
print(result)
#answer is 1969958987
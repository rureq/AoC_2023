#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()
all_maps = [[],[],[],[],[],[],[]]
i, j = 0, 0
mappings = data[3:]
seeds = data[0].replace('\n','').split(': ')[1].split(' ')

for line in mappings:
    if line[0].isdigit():
        all_maps[i].append(line.replace('\n', ''))
        j += 1
    elif line[0].isalpha():
        j = 0
        i += 1
    else:
        continue
    
for maps in all_maps:
    seeds2check = seeds.copy()
    for mapp in maps:
        mapp = mapp.split(' ')
        for seed_no, seed in enumerate(seeds2check):
            if int(seed) in range(int(mapp[1]), int(mapp[1])+int(mapp[2])):
                seeds[seed_no] = str(int(mapp[0]) + int(seed) - int(mapp[1]))

seeds = list(map(int,seeds))
print(min(seeds))
#answer is 600279879
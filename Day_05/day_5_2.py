#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
import re
input = open("input.txt", "r")
data = input.readlines()

seeds = data[0].replace('\n','').split(': ')[1].split(' ')

seed_ranges = []

for k in range(0,len(seeds),2):
    seed_ranges.append([])
    seed_range = [int(seeds[k]), int(seeds[k])+int(seeds[k+1])-1].copy()
    seed_ranges[int(k/2)] = seed_range
seed_ranges.sort(key = lambda x: x[0])

all_maps = [[]]
i= 0
for line in data[3:]:
    if line[0].isdigit():
        ranges = re.findall('[0-9]+', line)
        ranges = [int(x) for x in ranges]
        ranges = [ranges[0], ranges[0]+ranges[2]-1, ranges[1], ranges[1]+ranges[2]-1]
        all_maps[i].append(ranges)
        all_maps[i].sort(key = lambda x : x[2])
    elif line[0].isalpha():
        all_maps.append([])
        i += 1
    
for maps in all_maps:
    i = 0
    while i < len(seed_ranges):
        for map in maps:
            diff = map[0] - map[2]
            if seed_ranges[i][0] in range(map[2], map[3]+1) and seed_ranges[i][1] in range(map[2], map[3]+1):            
                seed_ranges[i] = [x + diff for x in seed_ranges[i]]
                break
            elif seed_ranges[i][0] in range(map[2], map[3]+1) and seed_ranges[i][1] not in range(map[2], map[3]+1):
                new_range_1 = [seed_ranges[i][0] + diff, map[3] + diff]
                new_range_2 = [map[3]+1, seed_ranges[i][1]]
                seed_ranges[i] = new_range_1
                seed_ranges.insert(i+1, new_range_2)
                break
            elif seed_ranges[i][0] not in range(map[2], map[3]+1) and seed_ranges[i][1] in range(map[2], map[3]+1):
                new_range_1 = [seed_ranges[i][0], map[2]-1]
                new_range_2 = [map[2] + diff, seed_ranges[i][1] + diff]
                seed_ranges[i] = new_range_2
                seed_ranges.insert(i, new_range_1)
                break
            elif seed_ranges[i][0] < map[2] and seed_ranges[i][1] > map[3]:
                new_range_1 = [seed_ranges[i][0], map[2]-1]
                new_range_2 = [map[2] + diff,map[3] + diff]
                new_range_3 = [map[3]+1, seed_ranges[i][1]]
                seed_ranges[i] = new_range_2
                seed_ranges.insert(i+1, new_range_3)
                seed_ranges.insert(i, new_range_1)
                break
        i+=1
        
res = []
for range in seed_ranges:
    res.append(range[0])

print(min(res))
#answer is 20191102
#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()

winning_nums = []
chosen_nums = []
hits = 0
no_of_ballots = len(data) * [1]


for line_num, line in enumerate(data):
    line = line.replace('\n', '')
    line = line.replace('  ', ' ')
    numbers = line.split(': ')[1]
    winning = numbers.split(" | ")[0].split(' ')
    chosen =  numbers.split(" | ")[1].split(' ')
    for numberw in winning:
        winning_nums.append(int(numberw))
    for numberc in chosen:
        chosen_nums.append(int(numberc))
    for num in chosen_nums:
        if num in winning_nums:
            hits += 1
    for i in range(hits):
        no_of_ballots[line_num+1+i] += no_of_ballots[line_num]
    numbers, winning, chosen, winning_nums, chosen_nums = [], [], [], [], []
    hits = 0
print(sum(no_of_ballots))
#answer: 5625994
    
    
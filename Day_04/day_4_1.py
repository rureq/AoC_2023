#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()

sum = 0
winning_nums = []
chosen_nums = []
power = -1

for line in data:
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
            power += 1
    if power > -1:
        sum += pow(2,power)
    power = -1
    numbers, winning, chosen, winning_nums, chosen_nums = [], [], [], [], []

print(sum)
#answer: 22193
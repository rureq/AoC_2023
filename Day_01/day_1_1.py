#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()
num = ""
two_dig_num = ""
numbers = []
for line in data:
    for c in line:
        if c.isdigit():
            num += c
    if num != "":
        if len(num) == 1:
            two_dig_num = num[0] + num[0]
        else:
            two_dig_num = num[0] + num[-1]
        numbers.append(int(two_dig_num))
        num = ""
        two_dig_num = ""
sum = sum(numbers) 
print(sum)

#answer is 53334
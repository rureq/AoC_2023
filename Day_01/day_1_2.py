#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()
modified_line = ""
numbers_only = ""
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
found = [100, 100, 100, 100, 100, 100, 100, 100, 100]
numbers = []

for line in data:
    modified_line = line
    while any(digit in modified_line for digit in digits):
        for index, digit in enumerate(digits):
            if modified_line.find(digit) != -1:            
                found[index] = modified_line.find(digit)
       
        lowest_num = min(found)
        modified_line = modified_line.replace(digits[found.index(lowest_num)], str(found.index(lowest_num)+1), 1)
        found = [100, 100, 100, 100, 100, 100, 100, 100, 100]
        
    for c in modified_line:
        if c.isdigit():
            numbers_only += c
    
    if len(numbers_only) != 0:
        if len(numbers_only) == 1:
            number = int(numbers_only[0] + numbers_only[0])
        else:
            number = int(numbers_only[0] + numbers_only[-1])
    numbers.append(number)
    numbers_only = ""
    
sum = sum(numbers) 
print(sum)

#answer is 52834
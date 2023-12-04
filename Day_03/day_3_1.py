#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()

sum = 0
temp_num = ''
chars2check = ''
check = 0

period_line = (len(data[0])) * '.'
data.insert(0,period_line)
data.append(period_line)
for num, line in enumerate(data):
    data[num]= '.' + line[:-1] +  '.'
data[-2] += '.'

for line_num, line in enumerate(data[1:-1]):
    for char_pos, char in enumerate(line):
        if char.isdigit() == 1:
            temp_num += char
            check = 1
        elif check == 1:            
            chars2check = (
            data[line_num][char_pos - len(temp_num)  -1 : char_pos +1] + 
            data[line_num + 1][char_pos - len(temp_num)-1] +
            data[line_num + 1][char_pos] +
            data[line_num + 2][char_pos -len(temp_num) -1 : char_pos +1])

            chars2check.translate({ord(i): None for i in '1234567890'})
            chars2check = chars2check.replace('.', '')            
        
            if len(chars2check) > 0:
                sum += int(temp_num)
                
            temp_num = ''
            check = 0
print(sum)
#the answer is 521601
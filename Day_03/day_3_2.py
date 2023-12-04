#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
input = open("input.txt", "r")
data = input.readlines()

sum = 0
start, stop = 0, 0
prev_start, prev_stop = 0, 0
ratio_list = []

period_line = (len(data[0])) * '.'
data.insert(0,period_line)
data.append(period_line)
for num, line in enumerate(data):
    data[num]= '.' + line[:-1] +  '.'
data[-2] += '.'

for line_num, line in enumerate(data[1:-1]):
    for char_pos, char in enumerate(line):
        if char == '*':
            for i in range(3):
                prev_start = char_pos -2
                prev_stop = char_pos -2
                for dig_num, digit in enumerate(data[line_num+i][char_pos-1:char_pos+2]):
                    start = char_pos + dig_num -1
                    stop = char_pos + dig_num -1
                    if stop > prev_stop:
                        if digit.isdigit():
                            while data[line_num+i][start].isdigit():
                                start -= 1
                            while data[line_num+i][stop+1].isdigit():
                                stop += 1
                            ratio_list.append(data[line_num+i][start+1:stop+1])
                            prev_start = start
                            prev_stop = stop
        if len(ratio_list) == 2:
            sum += int(ratio_list[0])*int(ratio_list[1])
        ratio_list = []
print(sum)
#the answer is 80694070
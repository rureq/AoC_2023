#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
from enum import Enum
input = open("input.txt", "r")
data = input.readlines()

dict = {
    'A' : 0x0E,
    'K' : 0x0D,
    'Q' : 0x0C,
    'J' : 0x0B,
    'T' : 0x0A,
    '9' : 0x09,
    '8' : 0x08,
    '7' : 0x07,
    '6' : 0x06,
    '5' : 0x05,
    '4' : 0x04,
    '3' : 0x03,
    '2' : 0x02
}
cards = []
set = []
result = 0

for i, line in enumerate(data):
    cards.append(['',[], [], []])
    cards[i][0] = line.split()[0]
    cards[i][3] = int(line.split()[1])
    hand = cards[i][0]
    bid = cards[i][3]
    while hand != '':
        char = hand[0]
        set.append(hand.count(char))
        hand = hand.replace(char, '')
    if len(set) == 1:
        cards[i][2] = 7 #'FiK'
    elif 4 in set:
        cards[i][2] = 6 #'FoK'
    elif 3 in set and 2 in set:
        cards[i][2] = 5 #'FH'
    elif 3 in set and 1 in set:
        cards[i][2] = 4 #'ToK'
    elif set.count(2) == 2:
        cards[i][2] = 3 #'TP'
    elif len(set) == 4:
        cards[i][2] = 2 #'OP'
    elif len(set) == 5:
        cards[i][2] = 1 #'HC'
    hand = cards[i][0]
    set = []
    cards[i][1] = [dict[hand[0]], dict[hand[1]], dict[hand[2]], dict[hand[3]], dict[hand[4]]]

cards.sort(key = lambda x:(x[2], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4]))

for it, card in enumerate(cards):
    result += (it+1) * card[3]
print(result)
#result is 248217452
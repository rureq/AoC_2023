#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
from enum import Enum
input = open("input.txt", "r")
data = input.readlines()
hands = []
bids = []
kinds = []
sets = []
types = []
ranks = []
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
no_of_hands = len(data)
cards = [['',[], '', []]] * no_of_hands
result = 0

for j, line in enumerate(data):
    hands.append(line.split()[0])
    bids.append(line.split()[1])

for i in range(no_of_hands):
    hand = hands[i]
    bid = bids[i]
    sets.append([])
    types.append([])
    # cards.append(['', [], '', []])
    print(hand)
    while hand != '':
        char = hand[0]
        sets[i].append(hand.count(char))
        hand = hand.replace(char, '')
    if len(sets[i]) == 1:
        types[i] = 7 #'FiK'
    elif 4 in sets[i]:
        types[i] = 6 #'FoK'
    elif 3 in sets[i] and 2 in sets[i]:
        types[i] = 5 #'FH'
    elif 3 in sets[i] and 1 in sets[i]:
        types[i] = 4 #'ToK'
    elif sets[i].count(2) == 2:
        types[i] = 3 #'TP'
    elif len(sets[i]) == 4:
        types[i] = 2 #'OP'
    elif len(sets[i]) == 5:
        types[i] = 1 #'HC'
    # print(sets[i])
    hand = hands[i]
    
    cards[i] = [hand, [dict[hand[0]], dict[hand[1]], dict[hand[2]], dict[hand[3]], dict[hand[4]]], types[i], int(bids[i])]
print('elo')
print(cards[0][1][0])
cards.sort(key = lambda x:(x[2], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4]))
print(hands)
print(types)
for it, card in enumerate(cards):
    result += (it+1) * card[-1]
    print(card)
print(result)
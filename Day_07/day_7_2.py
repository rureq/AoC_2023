#Advent of Code 2023, solution by Jerzy Piwkowski, https://github.com/rureq
def createSets(hand2check): #creates a set of numbers representing occurences of cards in hand
    set = []
    while hand2check != '':
        char = hand2check[0]
        set.append(hand2check.count(char))
        hand2check = hand2check.replace(char, '')
    return set

def checkType(set): #determine the type of hand based on set of cards in hand
    if len(set) == 1:
        return 7 #'FiK'
    elif 4 in set:
        return 6 #'FoK'
    elif 3 in set and 2 in set:
        return 5 #'FH'
    elif 3 in set and 1 in set:
        return 4 #'ToK'
    elif set.count(2) == 2:
        return 3 #'TP'
    elif len(set) == 4:
        return 2 #'OP'
    elif len(set) == 5:
        return 1 #'HC'

input = open("input.txt", "r")
data = input.readlines()

dict = {
    'A' : 0x0E,
    'K' : 0x0D,
    'Q' : 0x0C,
    'J' : 0x02,
    'T' : 0x0B,
    '9' : 0x0A,
    '8' : 0x09,
    '7' : 0x08,
    '6' : 0x07,
    '5' : 0x06,
    '4' : 0x05,
    '3' : 0x04,
    '2' : 0x03
}
cards = []
result = 0

for i, line in enumerate(data):
    cards.append(['',[], [], []])
    cards[i][0] = line.split()[0] #hand of cards
    cards[i][3] = int(line.split()[1]) #bid
    hand = cards[i][0]
    bid = cards[i][3]
    hand2check = hand
    if 'J' in hand: #when joker is found
        j_found = hand.count('J')
        if j_found == 5:
            hand2check = 'AAAAA'
        elif j_found == 4:
            hand2check = 5*hand.replace('J', '')
        elif j_found == 3:
            if hand.replace('J', '')[0] == hand.replace('J', '')[1]:
                hand2check = 5*hand.replace('J', '')[0]
            else:
                if dict[hand.replace('J', '')[0]] > dict[hand.replace('J', '')[1]]:
                    hand2check = 5*hand.replace('J', '')[0]
                else:
                    hand2check = 5*hand.replace('J', '')[1]
        elif j_found == 2:
            set2check = createSets(hand2check.replace('J', ''))
            if len(set2check) == 1:
                hand2check = 5*hand2check.replace('J', '')[0]
            elif len(set2check) == 2:
                replaced_hand = hand2check.replace('J', '')
                for ch in replaced_hand:
                    if replaced_hand.count(ch) == 2:
                        hand2check = hand2check.replace('J', ch)
                        break
            elif len(set2check) == 3:
                replaced_hand = hand2check.replace('J', '')
                hand2check = hand2check.replace('J', list(dict.keys())[list(dict.values()).index(max(dict[replaced_hand[0]],  dict[replaced_hand[1]], dict[replaced_hand[2]]))])
        elif j_found == 1:
            score = checkType(createSets(hand2check))
            for d in dict:
                if checkType(createSets(hand2check.replace('J', d[0]))) > score:
                    score = checkType(createSets(hand2check.replace('J', d[0])))
                    char2replace = d[0]
            hand2check = hand2check.replace('J', char2replace)
        else:
            pass
    hand = cards[i][0]
    cards[i][2] = checkType(createSets(hand2check)) #assigning type of hand
    cards[i][1] = [dict[hand[0]], dict[hand[1]], dict[hand[2]], dict[hand[3]], dict[hand[4]]] #assigning values to cards for sorting
    j_found = 0

cards.sort(key = lambda x:(x[2], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4])) #sorting by hand type and then by cards in hand

for it, card in enumerate(cards):
    result += (it+1) * card[3]
print(result)
#result is 245576185
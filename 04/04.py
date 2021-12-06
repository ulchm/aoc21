import re

from timeit import timeit

# lines = open('04.txt').readlines()
lines = open('04test.txt').readlines()
sequence =  [int(x) for x in lines[0].strip().split(',')]
lines = lines[2:]

def check_bingo(card, max):
    for x in range(5):
        found_bingo = True
        for y in range(5):
            if card[x][y] not in sequence[:max+1]:
                found_bingo=False
        if found_bingo:
            return True
    for y in range(5):
        found_bingo = True
        for x in range(5):
            if card[x][y] not in sequence[:max+1]:
                found_bingo=False
        if found_bingo:
            return True
    return False

def get_card_score(card, max):
    score = 0
    for x in range(5):
        for y in range(5):
            if card[x][y] not in sequence[:max+1]:
                score += card[x][y]
    return score * sequence[max]

def build_cards(input):
    all_cards = []
    current_card = []
    for l in input:
        if l.strip() != "":
            new_lines = [int(x) for x in re.split(r'\s+', l.strip())]
            current_card.append(new_lines)
        else:
            all_cards.append(current_card)
            current_card = []
        if l==input[len(input) - 1]:
            all_cards.append(current_card)
    return all_cards

def part1():
    cards = build_cards(lines)
    for i, called in enumerate(sequence):
        has_bingo = False
        for j, card in enumerate(cards):
            if check_bingo(card, i):
                print("Bingo on card {} at call {} with a {}".format(j, i, sequence[i]))
                print("Score: {}".format(get_card_score(card, i)))
                has_bingo=True
        if has_bingo:
            break

def part2():
    cards = build_cards(lines)
    for i, called in enumerate(sequence):
        has_bingo = False
        new_cards = []
        for j, card in enumerate(cards):
            if not check_bingo(card, i):
                new_cards.append(card)
            else:
                has_bingo=True
        if has_bingo:
            last_bingo = j
            last_bingo_number = i
            cards = new_cards
    print("The last bingo happened on card {} at turn {}".format(last_bingo, last_bingo_number))

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))

from collections import defaultdict
from timeit import timeit


def parseline(l):
    points = l.strip().split(' -> ')
    points = [tuple([int(i) for i in p.split(',')]) for p in points]
    return tuple(points)

lines = [parseline(l) for l in open('05.txt').readlines()]

def sign(n):
    return (n > 0) - (n < 0)

def get_diagonal_moves(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    return sign(dx), sign(dy), abs(x2-x1)

def part1():
    field = defaultdict(int)
    for p1, p2 in lines:
        if p1[0] == p2[0]:
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                field[(p1[0], y)] += 1
        elif p1[1] == p2[1]:
            for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                field[(x, p1[1])] += 1

    print(len([v for v in field.values() if v >= 2]))

def part2():
    field = defaultdict(int)
    for p1, p2 in lines:
        if p1[0] == p2[0]:
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                field[(p1[0], y)] += 1
        elif p1[1] == p2[1]:
            for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                field[(x, p1[1])] += 1
        else:
            sx, sy, steps = get_diagonal_moves(p1, p2)
            for i in range(steps+1):
                field[(p1[0]+sx*i, p1[1]+sy*i)] += 1

    print(len([v for v in field.values() if v >= 2]))

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))
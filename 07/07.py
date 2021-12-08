from collections import defaultdict, Counter

from timeit import timeit

lines = [int(x) for x in open('07.txt').readlines()[0].split(',')]
# lines = [int(x) for x in open('07test.txt').readlines()[0].split(',')]

def part1():
    counts = Counter(lines)
    differences = defaultdict(int)
    for i in range(max(lines)):
        for k,v in counts.items():
            if k > i:
                differences[i] += (k-i) * v
            elif k < i:
                differences[i] += (i-k) * v
    lowest = min(differences, key=differences.get)
    print("Level {} with {} fuel used.".format(lowest, differences[lowest]))

def get_fuel(current, target):
    fuel = 0
    if current > target:
        distance = abs(current - target)
        fuel = (distance / 2) * (1 + distance)
    elif current < target:
        distance = abs(target - current)
        fuel = (distance / 2) * (1 + distance)
    return fuel

def part2():
    counts = Counter(lines)
    differences = defaultdict(int)
    for i in range(max(lines)):
        for k,v in counts.items():
            if k > i:
                differences[i] += get_fuel(k, i) * v
            elif k < i:
                differences[i] += get_fuel(i, k) * v
    print(differences)
    lowest = min(differences, key=differences.get)
    print("Level {} with {} fuel used.".format(lowest, differences[lowest]))

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))

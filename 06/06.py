from timeit import timeit
from collections import defaultdict, Counter

sequence = [int(i) for i in open('06.txt').readlines()[0].split(',')]
# sequence = [int(i) for i in open('06test.txt').readlines()[0].split(',')]

def part1():
    pt1_sequence = list(sequence)
    for i in range(80):
        to_add = 0
        for j, s in enumerate(pt1_sequence):
            if s >= 1:
                pt1_sequence[j] -= 1
            if s == 0:
                pt1_sequence[j] = 6
                to_add += 1
        [pt1_sequence.append(8) for x in range(to_add)]
    print("Total of {} fish!".format(len(pt1_sequence)))

def part2():
    counts = Counter(sequence)
    for i in range(256):
        new_dict = defaultdict(int)
        for k,v in counts.items():
            if k != 0:
                new_dict[k-1] += v
            else:
                new_dict[6] += v
                new_dict[8] = v
        counts = new_dict
    total = 0
    for k,v in counts.items():
        total += v
    print(total)

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))

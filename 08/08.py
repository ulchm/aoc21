from timeit import timeit

lines = open('08.txt').readlines()
# numbers = [int(x) for x in open('01.txt').readlines()]

def part1():
    right_side = [line.split(' | ')[1].strip() for line in lines]
    total = 0
    for line in right_side:
        for seq in line.split(' '):
            if len(seq) == 2 or len(seq) == 3 or len(seq) == 4 or len(seq) == 7:
                total += 1
    print("1, 4, 7, 8 appear a total of: {} times".format(total))


def part2():
    pass

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))

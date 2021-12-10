from timeit import timeit

lines = [x.strip() for x in open('10.txt').readlines()]

tags = ['{}', '<>', '[]', '()']
openers = ['{', '<', '[', '(']
closers = [('}',1197), ('>', 25137), (']', 57), (')', 3)]


def strip_matches(line):
    found = True
    while found:
        found = False
        for tag in tags:
            if line.find(tag) != -1:
                line = line.replace(tag, '')
                found = True
    return line

def is_corrupt(line):
    found = False
    for c in line:
        for k,v in closers:
            if c == k:
                found = True
    return found

def calculate(line):
    for c in line:
        for k,v in closers:
            if c == k:
                return v


def part1():
    print(len(lines))
    part1_lines = list(lines)
    score = 0
    for l in part1_lines:
        stripped_line = strip_matches(l)
        if is_corrupt(stripped_line):
            score += calculate(stripped_line)
    print(score)


def part2():
    pass

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))

from timeit import timeit

lines = open('02.txt').readlines()

def part1():
    forward = 0
    depth = 0
    for line in lines:
        direction, units = str.split(line)
        if direction == "up":
            depth -= int(units)
        elif direction == "down":
            depth += int(units)
        else:
            forward += int(units)
    print("Grand Total: {}".format(depth * forward))

def part2():
    forward = 0
    aim = 0
    depth = 0
    for line in lines:
        direction, units = str.split(line)
        if direction == "up":
            aim -= int(units)
        elif direction == "down":
            aim += int(units)
        else:
            forward += int(units)
            depth += aim * int(units)
    print("Grand Total: {}".format(depth * forward))

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))

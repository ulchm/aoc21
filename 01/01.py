from timeit import timeit

lines = open('01.txt').readlines()
numbers = [int(x) for x in open('01.txt').readlines()]

def get_increment_count(input):
    increased = 0
    for k,v in enumerate(input[1:], start=1):
        if v > input[k-1]:
            increased += 1
    return increased

def part1():
    print("increased {} times".format(get_increment_count(numbers)))

def part2():
    newlist = []
    for k,v in enumerate(numbers):
        try:
            newlist.append(v+numbers[k+1]+numbers[k+2])
        except IndexError:
            break
    print("Increased {} times".format(get_increment_count(newlist)))

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))

from collections import defaultdict
from timeit import timeit

lines = [l.strip() for l in open('day03.txt').readlines()]
nums = [int(l, 2) for l in lines]

def invert(n, l):
    return ~n & ((1 << l) - 1)


def get_most_common_at_pos(nums, pos):
    ones = 0
    zeros = 0
    for num in nums:
        if num[pos] == '1':
            ones += 1
        else:
            zeros += 1
    if ones >= zeros:
        return '1'
    return '0'

def get_least_common_at_pos(nums, pos):
    ones = 0
    zeros = 0
    for num in nums:
        if num[pos] == '1':
            ones += 1
        else:
            zeros += 1
    if zeros <= ones:
        return '0'
    return '1'


def part1():
    ans = ''
    for i in range(len(lines[0])):
        count = 0
        for l in lines:
            count += 1 if l[i] == '1' else 0
        if count >= len(lines) / 2:
            ans += '1'
        else:
            ans += '0'
    gamma = int(ans, 2)
    epsilon = invert(gamma, len(lines[0]))
    print(epsilon * gamma)


def part2():
    o2_pool = list(lines)
    co2_pool = list(lines)

    l = len(lines[0])
    for i in range(l):
        if len(o2_pool) > 1:
            mc = get_most_common_at_pos(o2_pool, i)
            o2_pool = [n for n in o2_pool if n[i] == mc]
        if len(co2_pool) > 1:
            lc = get_least_common_at_pos(co2_pool, i)
            co2_pool = [n for n in co2_pool if n[i] == lc]
    print(int(o2_pool[0], 2) * int(co2_pool[0], 2))



if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))


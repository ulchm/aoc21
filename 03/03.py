from timeit import timeit

lines = open('03.txt').readlines()

def get_gamma_and_epsilon(input):
    chars = [0,0,0,0,0,0,0,0,0,0,0,0]
    for line in input:
        for i, char in enumerate(line):
            if i < 12:
                if int(char) == 1:
                    chars[i] += 1
                else:
                    chars[i] -= 1
    gamma = ""
    epsilon = ""
    for c in chars:
        if c > 0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return(int(gamma,2), int(epsilon,2))

def part1():
    gamma, epsilon = get_gamma_and_epsilon(lines)
    print("Gamma * Epsilon = {}".format(gamma * epsilon))

def get_oxygen_levels(input, slot):
    total = 0
    for line in input:
        if int(line[slot]) == 1:
            total += 1
        else:
            total -= 1
    if total >= 0:
        return 1
    return 0

def get_co2_levels(input, slot):
    total = 0
    for line in input:
        if int(line[slot]) == 1:
            total += 1
        else:
            total -= 1
    if total >= 0:
        return 0
    return 1

def part2():
    oxygen_list = list(lines)
    co2_list = list(lines)
    for i in range(0,12):
        most_used = get_oxygen_levels(oxygen_list, i)
        new_o2 = []
        for j in oxygen_list:
            if j[i] == (str(most_used)):
                new_o2.append(j.strip())
        oxygen_list = new_o2
    o2_val = int(oxygen_list[0], 2)

    for i in range(0,12):
        least_used = get_co2_levels(co2_list, i)
        new_co2 = []
        for j in co2_list:
            if j[i] == (str(least_used)):
                new_co2.append(j.strip())
        co2_list = new_co2
        if len(co2_list) == 1:
            break
    co2_val = int(co2_list[0], 2)
    print("Life Support Rating: {}".format(o2_val * co2_val))

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))

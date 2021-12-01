import os
base_path = os.getcwd()
file_text = """from timeit import timeit

lines = open('%DAY%.txt').readlines()
# numbers = [int(x) for x in open('%DAY%.txt').readlines()]

def part1():
    pass

def part2():
    pass

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))
"""

i = 1
while i <= 31:
    day = f'{i:02}'
    path = os.path.join(base_path, day)
    try:
        os.mkdir(path)
        os.chdir(path)
        f=open("{}.txt".format(day), "w+")
        f.close()
        f=open("{}.py".format(day),"w+")
        file_text = file_text.replace("%DAY%", day)
        f.write(file_text)
        f.close()
        os.chdir(base_path)
    except OSError:
        print("Creating of the directory {} failed.  Folder already exists?".format(path))
    i+=1

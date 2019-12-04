filename = "day1.txt"

with open(filename) as f:
    lines = f.read().splitlines()
    lines = list(map(int, lines))

lines = map(lambda x: ((x // 3) - 2), lines)
total_mass = sum(lines)
print(total_mass)

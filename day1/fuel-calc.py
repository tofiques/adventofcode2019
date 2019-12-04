filename = "day1.txt"

with open(filename) as f:
    lines = f.read().splitlines()
    lines = list(map(int, lines))

result = map(lambda x: ((x // 3) - 2), lines)
total_mass = sum(result)
print(total_mass)

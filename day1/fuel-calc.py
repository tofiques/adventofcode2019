filename = "day1.txt"

with open(filename) as f:
    lines = f.read().splitlines()
    lines = list(map(int, lines))


def calculate_fuel(x):
    mass = ((x // 3) - 2)
    return mass


def calc_part_two(mass,total=0):

    added_fuel = calculate_fuel(mass)
    total += added_fuel
    if (calculate_fuel(added_fuel)-2) > 0:
        return calc_part_two(mass=added_fuel, total=total)
    return total

part_one = map(calculate_fuel, lines)
part_two = map(calc_part_two, lines)
total_mass_part_one = sum(part_one)
total_mass_part_two = sum(part_two)
print(total_mass_part_one)
print(total_mass_part_two)

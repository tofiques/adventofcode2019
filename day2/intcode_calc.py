from itertools import product

filename = "dataset.txt"

with open(filename) as f:
    lines = f.read().split(",")
    lines = list(map(int, lines))


def calc_int(lines, noun, verb):
    data=lines.copy()
    data[1] = noun
    data[2] = verb
    for i in range(0, len(data) - 1, 4):
        one = data[i]
        two = data[i + 1]
        three = data[i + 2]
        four = data[i + 3]
        if (one == 1):
            data[four] = data[two] + data[three]
        elif (one == 2):
            data[four] = data[two] * data[three]
        elif (one == 99):
            break

    return data[0]



print((calc_int(lines, 12, 2)))

for noun, verb in product(range(0, 100), range(0, 100)):
    if calc_int(lines,noun, verb) == 19690720:
        print( 100 * noun + verb)
        break

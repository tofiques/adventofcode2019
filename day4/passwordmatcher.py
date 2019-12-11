def password_adjacent_criteria(x):
    matches_pass = False

    for x, y in zip(x[::], x[1::]):
        if x == y:
            matches_pass = True
            break
    return matches_pass;


def password_increasing_criteria(x):
    matches_pass = True

    for x, y in zip(x[::], x[1::]):
        if y < x:
            matches_pass = False
            break
    return matches_pass;


def calculate_num_passwords():
    count = 0
    range_num = list(range(146810, 612564))
    for x in range_num:
        password_number = list(str(x))
        password_number = list(map(int, password_number))
        if (password_adjacent_criteria(password_number) and password_increasing_criteria(password_number)):
            count += 1

    return (count)


print(calculate_num_passwords())

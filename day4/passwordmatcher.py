from collections import Counter


def password_adjacent_criteria(num_list):
    matches_pass = False

    for x, y in zip(num_list[::], num_list[1::]):
        if x == y:
            matches_pass = True
            break
    return matches_pass


def password_increasing_criteria(x):
    matches_pass = True

    for x, y in zip(x[::], x[1::]):
        if y < x:
            matches_pass = False
            break
    return matches_pass


def has_exact_double(password: str):
    return any(count == 2 for _, count in Counter(password).most_common())


def calculate_num_passwords():
    count = 0
    range_num = list(range(146810, 612565))
    for x in range_num:
        password_number = list(str(x))
        password_number = list(map(int, password_number))
        if password_adjacent_criteria(password_number) and password_increasing_criteria(password_number):
            matching_count = Counter(password_number)
            list_counter = matching_count.values()
            for state in list_counter:
                if state == 2:
                    count += 1
                    break

    return count


print(calculate_num_passwords())

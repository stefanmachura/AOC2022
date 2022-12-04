from helpers import get_file


pairs = get_file("04")


def is_contained(pair):
    first, second = pair.split(",")
    first_span = [int(x) for x in first.split("-")]
    second_span = [int(x) for x in second.split("-")]

    first_list = set(range(first_span[0], first_span[1] + 1))
    second_list = set(range(second_span[0], second_span[1] + 1))

    return bool(set(first_list) & set(second_list))


result = 0

for pair in pairs:
    if is_contained(pair):
        result += 1

print(result)

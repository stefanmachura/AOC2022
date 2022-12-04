from helpers import get_file


pairs = get_file("04")


def is_contained(pair):
    first, second = pair.split(",")
    first_span = [int(x) for x in first.split("-")]
    second_span = [int(x) for x in second.split("-")]

    if first_span[0] >= second_span[0] and first_span[1] <= second_span[1]:
        return True

    if second_span[0] >= first_span[0] and second_span[1] <= first_span[1]:
        return True


result = 0

for pair in pairs:
    if is_contained(pair):
        result += 1

print(result)

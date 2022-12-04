from helpers import get_file, letter_to_value

result = 0

backpacks = get_file("03")

threes = []
counter = 0
tmp_list = []
for backpack in backpacks:
    tmp_list.append(backpack)
    counter += 1
    if counter == 3:
        threes.append(tmp_list)
        counter = 0
        tmp_list = []


for three in threes:
    a, b, c = three
    a = set(a)
    b = set(b)
    c = set(c)

    common = a & b & c
    common = next(iter(common))
    result += letter_to_value(common)

print(result)

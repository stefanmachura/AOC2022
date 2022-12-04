from helpers import get_file, letter_to_value

result = 0

backpacks = get_file("03")

for backpack in backpacks:
    half = len(backpack) // 2
    first = set(backpack[:half])
    second = set(backpack[half:])
    common = first & second
    common = next(iter(common))

    result += letter_to_value(common)

print(result)

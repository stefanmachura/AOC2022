from helpers import get_file

lines = get_file("05")

separator = lines.index("")

boxes = lines[:separator]
moves = lines[separator:]

n = int(boxes.pop().split(" ")[-1])

filled = []

filled_box_list = []

for box in boxes:
    filled_box_row = []
    box_list = box.split("    ")
    for x in box_list:
        filled_box_row.extend(x.split(" "))
    while len(filled_box_row) < n:
        filled_box_row.append("")
    filled_box_list.append(filled_box_row)


stacks = []

for x in filled_box_list:
    assert len(x) == n

for column in range(n):
    new_column = []
    for x in filled_box_list:
        new_column.append(x[column])
    new_column = [x for x in new_column if x != ""]
    stacks.append(new_column)


moves.pop(0)

parsed_moves = []

for move in moves:
    move_list = move.split(" ")
    parsed_moves.append(
        [int(move_list[1]), int(move_list[3]) - 1, int(move_list[5]) - 1]
    )


for move in parsed_moves:
    how_many, from_, to = move

    moving_boxes = stacks[from_][:how_many]
    stacks[from_] = stacks[from_][how_many:]
    stacks[to] = moving_boxes + stacks[to]


result = "".join([stack[0] for stack in stacks])

result = result.replace("[", "")
result = result.replace("]", "")

print(result)

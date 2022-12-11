from helpers import get_file

forest = get_file("08")

rows = forest

columns = []

for x in range(len(rows[0])):
    c = []
    for row in rows:
        c.append(row[x])
    columns.append("".join(c))


print(rows)
print(columns)

result = ((len(rows) - 1) * 2) + ((len(columns) - 1) * 2)

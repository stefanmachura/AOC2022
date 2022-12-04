with open("day01.input", "r") as inp:
    elf_list = inp.readlines()

elf_list = [e.rstrip() for e in elf_list]

elf_list_clean = []

for e in elf_list:
    if e == "":
        elf_list_clean.append(0)
        continue
    elf_list_clean.append(int(e))

results = []

temp = 0
for e in elf_list_clean:
    temp += e
    if e == 0:
        results.append(temp)
        temp = 0

print(max(results))

best_three = sum(sorted(results, reverse=True)[0:3])

print(best_three)

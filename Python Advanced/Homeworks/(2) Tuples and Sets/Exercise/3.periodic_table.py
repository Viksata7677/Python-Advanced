table = set()

for i in range(int(input())):
    for el in input().split():
        table.add(el)

print(*table, sep="\n")
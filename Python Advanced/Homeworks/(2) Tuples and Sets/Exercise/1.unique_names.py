names_count = int(input())
names = set()

for i in range(names_count):
    names.add(input())

print(*names, sep="\n")
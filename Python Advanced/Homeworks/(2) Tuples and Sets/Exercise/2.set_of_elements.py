n, m =[int(x) for x in input().split()]

first_set = {input() for i in range(n)}
second_set = {input() for i in range(m)}

print(*first_set.intersection(second_set), sep="\n")

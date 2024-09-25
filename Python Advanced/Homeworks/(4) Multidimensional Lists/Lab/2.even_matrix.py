row_count = int(input())

matrix = []

for i in range(row_count):
    data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(data)

# even_matrix = []
#
# for row in matrix:
#     sub_list = []
#     for el in row:
#         if el % 2 == 0:
#             sub_list.append(el)

print(matrix)

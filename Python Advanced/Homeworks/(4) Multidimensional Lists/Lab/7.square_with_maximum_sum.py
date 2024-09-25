row, col = [int(el) for el in input().split(", ")]

matrix = []

for i in range(row):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = float('-inf')
sum_matrix = []

for row_index in range(row-1):
    for col_index in range(col-1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index+1]
        element_under = matrix[row_index+1][col_index]
        element_diagonal = matrix[row_index+1][col_index+1]

        total_sum = current_element + next_element + element_under + element_diagonal

        if max_sum < total_sum:
            max_sum = total_sum
            sum_matrix = [[current_element, next_element], [element_under, element_diagonal]]

print(*sum_matrix[0])
print(*sum_matrix[1])
print(max_sum)

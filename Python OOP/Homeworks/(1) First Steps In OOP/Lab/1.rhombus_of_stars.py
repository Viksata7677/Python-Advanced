n = int(input())


def print_row(size, row):
    print(" " * (size - row), "* " * row)


def print_upper_rhombus_part(size):
    for row in range(1, n +1):
        print(" " * (n-row), "* "*row)


def print_bottom_rhombus_part(size):
    for row in range(size-1, 0, -1):
        print(" " * (size-row), "* "*row)


def print_rhombus(size):
    print_upper_rhombus_part(size)
    print_bottom_rhombus_part(size)

print_rhombus(n)
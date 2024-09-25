def print_airspace(airspace):
    airspace = ["".join(row) for row in airspace]
    output = "\n".join(airspace)
    print(output)

N = int(input())
airspace = []
jet_row, jet_col = 0, 0
for i in range(N):
    row = input()
    try:
        jet_col = row.index('J')
        jet_row = i
    except ValueError:
        pass
    airspace.append(list(row))
jet_health = 300
enemies_left = 4

while True:
    command = input()
    new_row, new_col = jet_row, jet_col
    if command == "up":
        new_row = max(0, jet_row-1)
    elif command == "down":
        new_row = min(N-1, jet_row+1)
    elif command == "left":
        new_col = max(0, jet_col-1)
    elif command == "right":
        new_col = min(N-1, jet_col+1)

    entity = airspace[new_row][new_col]
    if entity == "E":
        jet_health -= 100
        enemies_left -= 1
    elif entity == "R":
        jet_health = 300
    airspace[jet_row][jet_col] = '-'
    airspace[new_row][new_col] = 'J'
    jet_row, jet_col = new_row, new_col

    if jet_health == 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_row}, {jet_col}]!")
        break
    elif enemies_left == 0:
        print("Mission accomplished, you neutralized the aerial threat!")
        break

print_airspace(airspace)
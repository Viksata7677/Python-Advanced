money_seq = [int(x) for x in input().split()]
prices_seq = [int(x) for x in input().split()]
foods_bought = 0

while money_seq and prices_seq:
    money = money_seq.pop()
    price = prices_seq.pop(0)
    if money == price:
        foods_bought += 1
    elif money > price:
        foods_bought += 1
        diff = money - price
        if money_seq:
            money_seq[-1] += diff
        else:
            money_seq.append(diff)
    else:
        pass

if foods_bought >= 4:
    print(f"Gluttony of the day! Henry ate {foods_bought} foods.")
elif foods_bought > 1:
    print(f"Henry ate: {foods_bought} foods.")
elif foods_bought == 1:
    print(f"Henry ate: 1 food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
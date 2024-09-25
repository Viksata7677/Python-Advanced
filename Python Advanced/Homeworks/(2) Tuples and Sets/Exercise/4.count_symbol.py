# occurrrences = {}
#
# for symbol in input():
#     occurrrences[symbol] = occurrrences.get(symbol, 0) + 1
#
# for symbol, times in sorted(occurrrences.items()):
#     print(f"{symbol}: {times} time/s")
#

text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")
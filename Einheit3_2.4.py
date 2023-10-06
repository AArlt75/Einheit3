numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

for x in range(1, 5):
    nrs = numbers[:x]
    print(" ".join(nrs))
    for y in range(x):
        numbers.remove(numbers[0])
numbers = [5, 8, 9, 1, 3]
srebmun = []

for x in range(len(numbers) - 1, -1, -1):
    srebmun.append(str(numbers[x]))

print(", ".join(srebmun))
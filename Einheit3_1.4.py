word = "Ramtin"
drow = []

for x in range(len(word) - 1, -1, -1):
    drow.append(word[x])

print("".join(drow).capitalize())
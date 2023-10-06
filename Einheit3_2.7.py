vocals = ["a", "e", "i", "o", "u"]
liste = ["Ramtin", 3, "3", "Hallo", "Alexander"]
count = 0

for x in liste:
    for y in str(x):
        if y in vocals:
            count += 1

print(count)
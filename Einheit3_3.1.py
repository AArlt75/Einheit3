liste = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2, 3], [4, 5, 6], [2, 3, 4], [5, 6, 7], [6, 7, 8], [1, 2, 3]]

liste.sort()
x = 0

while x in range(len(liste) - 1):
    if liste[x] == liste [x + 1]:
        liste.remove(liste[x + 1])
    else:
        x += 1

print(liste)
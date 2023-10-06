from pathlib import Path
import os

print("Zum Wörter zählen stehen 5 Textdokumente zur Auswahl:\n")

current_wd = Path.cwd()
sourcedir = Path(current_wd.parent / "Dateien")
textfiles = os.listdir(sourcedir)
textfiles.sort()
for txt in textfiles:
    if len(txt) == 5:
        print(f"\t- {txt}")

choose = ["1", "2", "3", "4", "5"]

while True:
    document = input("\nGeben sie eine Zahl (1 - 5) zur Auswahl eines Dokumentes an: ")
    if document not in choose:
        print("Fehlerhafte Eingabe! Bitte wiederholen!")
    else:
        break

text = ""

with open(f"{sourcedir/document}.txt", "r") as file:
    for word in file:
        if word == "\n":
            continue
        else:
            text = text + word
    
count_word = text.split(" ")
print(f"\nDie Datei {document}.txt hat {len(count_word)} Wörter")
print("------------------------------")
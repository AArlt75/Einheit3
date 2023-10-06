word = "restart"
replaced_word = []
vocals = ["a", "e", "i", "o", "u"]

for x in range(len(word)):
    if word[x] in vocals:
        replaced_word.append("$")
    else:
        replaced_word.append("%")
        
print(''.join(replaced_word))
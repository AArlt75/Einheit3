word = "restart"
replaced_word = ["r"]

for x in range(1, len(word)):
    if word[x] == word[0]:
        replaced_word.append("$")
    else:
        replaced_word.append(word[x])
        
print(''.join(replaced_word))
text_original = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
text = text_original.replace(",", "")
textlist = text.split(" ")
mean = 0

for word in textlist:
    mean = mean + len(word) / len(textlist)

print(mean)
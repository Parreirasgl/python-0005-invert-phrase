# Inverter uma palavra sem usar função reverse
# Invert a word without using reverse function
word = input()
list_word = list(word)
length = len(word)

for i in range(length):
    last_letter = list_word[length - 1]
    list_word.pop(length - 1)
    list_word.insert(i, last_letter)

new_word = "".join(list_word)
print(new_word)




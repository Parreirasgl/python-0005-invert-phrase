# Inverter uma palavra sem usar funções nativas list and reverse.
# Invert a word without using native function called list and reverse.

def word_to_list(word):
    list_word = []
    for i in word:
        list_word.append(i)
    return list_word

def invert_list(list_word):
    length = len(list_word)
    for i2 in range(length):
        last_letter = list_word[length - 1]
        list_word.pop(length - 1)
        list_word.insert(i2, last_letter)
    return list_word

word = input()
new_word = "".join(invert_list(word_to_list(word)))
print(new_word)




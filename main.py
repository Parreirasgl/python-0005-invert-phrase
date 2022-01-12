# Inverter uma palavra sem usar funções nativas list or join or reverse.
# Invert a word without using native functions called list or join or reverse.

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

def join_list(list_word):
    new_word = ""
    for i3 in list_word:
        new_word += i3
    return new_word

word = input()
final_word = join_list(invert_list(word_to_list(word)))
print(final_word)



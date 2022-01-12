# Inverter uma palavra sem usar funções nativas.
# Invert a word without using native functions.

def word_to_list(word):
    list_word = []
    for i in word:
        list_word.append(i)
    return list_word

def delete_item(list, position):
    new_list = []
    for i4 in range(len(list)):
        if position == i4:
            pass
        else:
            new_list.append(list[i4])
    return new_list

def insert_item(list, position, item):
    new_list = []
    for i5 in range(len(list) + 1):
        if i5 == len(list):
            if position == i5:
                new_list.append(item)
            else:
                pass
        elif position == i5:
            new_list.append(item)
            new_list.append(list[i5])
        else:
            new_list.append(list[i5])
    return new_list

def invert_list(list_word):
    length = len(list_word)
    for i2 in range(length):
        last_letter = list_word[length - 1]
        list_word = delete_item(list_word, length-1)
        list_word = insert_item(list_word, i2, last_letter)
    return list_word

def join_list(list_word):
    new_word = ""
    for i3 in list_word:
        new_word += i3
    return new_word

word = input()
final_word = join_list(invert_list(word_to_list(word)))
print(final_word)



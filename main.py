# Invert a word or phrase without using native functions.
# Inverter uma palavra ou frase sem usar funções nativas.

def word_to_list(word):
    """Transform word to list.
    Transforma palavra em lista.
    """
    list_word = []
    for i in word:
        list_word.append(i)
    return list_word


def delete_item(list, position):
    """Delete item from list.
    Deleta item da lista.
    """
    new_list = []
    for i4 in range(len(list)):
        if position == i4:
            pass
        else:
            new_list.append(list[i4])
    return new_list


def insert_item(list, position, item):
    """Insert item in list.
    If item is inserted in the middle of the list, it push others.
    The item can be inserted after the last item in the list.
    Insere item em lista.
    Se item é iserido no meio da lista, empurra outros.
    O item pode ser inserido após o último item da lista.
    """
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
    """Invert items in list.
    To do this, it does a for loop through the length of the list.
    Then save the last value of the list; then deletes last value;
    then insert last value in the right place
    Inverte itens na lista.
    Para isso, faz um for loop pelo comprimento da lista.
    Depois guarda último valor da lista; depois deleta último valor;
    depois insere último valor no lugar certo.
    """
    length = len(list_word)
    for i2 in range(length):
        last_letter = list_word[length - 1]
        list_word = delete_item(list_word, length-1)
        list_word = insert_item(list_word, i2, last_letter)
    return list_word


def join_list(list_word):
    """Turns list into word.
    Transforma lista em palavra.
    """
    new_word = ""
    for i3 in list_word:
        new_word += i3
    return new_word


word = input()
final_word = join_list(invert_list(word_to_list(word)))
print(final_word)



ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHA_UP = ALPHABET.upper()

"""
··A··
·B·B·
C···C
·B·B·
··A··


····A····
···B·B···
··C···C··
·D·····D·
E·······E
·D·····D·
··C···C··
···B·B···
····A····


"""
def row_maker(current_letter, input_latter) -> tuple:
    index_curentletter = ALPHA_UP.index(current_letter)
    index_inputletter = ALPHA_UP.index(input_latter)
    letters_delta = index_inputletter -index_curentletter
    row:list = []
    for index in range(index_inputletter * 2 + 1):
        row.append('.')
    row[letters_delta] = current_letter
    row[-1 *(letters_delta +1)]  = current_letter
    my_row = ''.join(row)
    return (my_row)




def rows(letter:str) -> None:
    index_inputletter = ALPHA_UP.index(letter)
    list_of_rows:list = []

    for index in range(index_inputletter + 1):
        list_of_rows.append(row_maker(ALPHA_UP[index], letter))
    for index in range(index_inputletter-1, -1, -1):
        temp_row = list_of_rows[index]
        list_of_rows.append(temp_row)

    for item in list_of_rows:
        print(item)



rows('N')



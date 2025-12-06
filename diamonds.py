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
    number_of_row = index_curentletter + 1
    row:list = []
    for index in range(index_inputletter * 2 + 1):
        row.append('.')
    row[letters_delta] = current_letter
    row[-1 *(letters_delta +1)]  = current_letter
    my_row = ''.join(row)
    return (number_of_row, my_row)


def rows(letter:str) -> None:
    index_inputletter = ALPHA_UP.index(letter)
    list_of_rows:list = []

    for index in range(index_inputletter + 1):
        list_of_rows.append(row_maker(ALPHA_UP[index], letter))
    new_row_number = list_of_rows[-1][0] + 1
    for index in range(index_inputletter-1, -1, -1):
        temp_row = (new_row_number,list_of_rows[index][1])
        list_of_rows.append(temp_row)
        new_row_number += 1


    for item in list_of_rows:
        print(item[1])






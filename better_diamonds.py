ALPHA_UP = 'abcdefghijklmnopqrstuvwxyz'.upper()

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

def row_maker(line_size,current_letter) -> str:
    row:list = []
    for index in range(line_size):
        row.append(' ')
    if ALPHA_UP.index(current_letter) == 0:
        row[(line_size-1)//2] = current_letter
    else:
        row[(line_size - 1)//2 - ALPHA_UP.index(current_letter)] = current_letter
        row[(line_size - 1)//2 + ALPHA_UP.index(current_letter)] = current_letter


    return ''.join(row)


def rows(letter:str) -> list:
    res:list = []
    line_size = ALPHA_UP.index(letter) * 2 + 1
    for index in range(ALPHA_UP.index(letter) + 1):
        res.append(row_maker(line_size, ALPHA_UP[index]))
    for index in range (len(res) -2, -1, -1):
        res.append(res[index])
    return res

# print(rows('N'))
"""
·*·*·
··*··
··*··
·····


1*3*1
13*31
·2*2·
·111·

"""

def get_position(garden:list,position:tuple) ->tuple:
    POSITIONS = ('top','bottom','right','left''center')
    rows_len:int = len(garden[0])
    columns_len:int = len(garden)
    res:tuple
    match (position):
        case (0,0):
            res = ('top','left')
        case (0,y) if (y != 0)and (y != rows_len -1) :
            res = ('top','center')
        case (0,y) if y == rows_len -1:
            res = ('top','right')

        case (x,0) if (x != 0) and (x != columns_len -1)  :
            res = ('center','left')
        case (x,y) if (x != 0) and (x != columns_len -1) and (y != 0) and (y != rows_len -1):
            res = ('center','center')
        case (x,y) if (x != 0) and (x != columns_len -1) and (y == rows_len - 1):
            res = ('center','right')


        case(x,0) if x == columns_len - 1:
            res = ('bottom','left')
        case (x,y) if (x == columns_len - 1) and (y != 0)and (y != rows_len -1) :
            res = ('bottom','center')
        case (x,y)if (x == columns_len - 1) and (y == rows_len - 1):
            res = ('bottom','right')

    return res

def annotate(garden:list[str]) -> None:
    len_check: int = 0
    position:tuple = ()

#Checking for invalid input
    for item in garden:
        if item is garden[0]:
            len_check = len(item)
        if len(item) != len_check:
            raise ValueError("The board is invalid with current input.")

    for index_of_rows, row in enumerate(garden):
        new_row = list(row)
        for index_of_char, char in enumerate(new_row):
            if (new_row[index_of_char] != ' ') and (new_row[index_of_char] !=  '*'):
                raise ValueError("The board is invalid with current input.")

# if the first and left and last line, then only 2 rows of dependant positions
# if left or right column, -> 2 columns of dependant positions


    for index_of_rows, row in enumerate(garden):
        new_row = list(row)
        for index_of_char, char in enumerate(new_row):
            if new_row[index_of_char] == ' ':
                new_row[index_of_char] = '0'
        garden[index_of_rows] = new_row
# if 1 row
# if 1 row 1 column

    for index_of_row, row in enumerate(garden):
        for index_of_char, char in enumerate(row):
            position = get_position(garden,(index_of_row, index_of_char))
            if char == '*':
                if position == ('top', 'left'):
                    chars_to_change = [(index_of_row,index_of_char+1),
                                       (index_of_row+1,index_of_char),
                                       (index_of_row + 1,index_of_char + 1)
                                       ]


                    if len(garden) == 1:
                        for _ in range (2):
                            chars_to_change.pop()

                    elif len(row) == 1:
                        chars_to_change.pop(0)
                        chars_to_change.pop()


                    for item in chars_to_change:
                        if garden[item[0]][item[1]] != '*':
                            garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]])+1)
                elif position == ('top', 'center'):
                     chars_to_change = [(index_of_row, index_of_char -1),
                                        (index_of_row, index_of_char + 1),
                                        (index_of_row+1, index_of_char -1),
                                        (index_of_row + 1, index_of_char),
                                        (index_of_row + 1, index_of_char + 1)
                                        ]
                     if len(garden) == 1:
                         for _ in range(3):
                            chars_to_change.pop()

                     for item in chars_to_change:
                         if garden[item[0]][item[1]] != '*':
                             garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]]) + 1)
                elif position == ('top', 'right'):
                    chars_to_change = [(index_of_row, index_of_char - 1),
                                       (index_of_row + 1, index_of_char - 1),
                                        (index_of_row + 1, index_of_char)
                                       ]
                    if len(garden) == 1:
                        for _ in range(2):
                            chars_to_change.pop()

                    for item in chars_to_change:
                        if garden[item[0]][item[1]] != '*':
                            garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]]) + 1)

                elif position == ('center', 'left'):
                    chars_to_change = [(index_of_row-1,index_of_char),
                                       (index_of_row-1,index_of_char+1),
                                       (index_of_row,index_of_char+1),
                                       (index_of_row+1,index_of_char),
                                       (index_of_row + 1,index_of_char + 1)
                                       ]

                    if len(row) == 1:
                        chars_to_change.pop(1)
                        chars_to_change.pop(1)
                        chars_to_change.pop()



                    for item in chars_to_change:
                        if garden[item[0]][item[1]] != '*':
                            garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]]) + 1)
                elif position == ('center', 'center'):
                    chars_to_change = [(index_of_row - 1, index_of_char-1),
                                       (index_of_row - 1, index_of_char),
                                       (index_of_row - 1, index_of_char + 1),
                                       (index_of_row,index_of_char-1),
                                       (index_of_row, index_of_char + 1),
                                       (index_of_row+1,index_of_char-1),
                                       (index_of_row + 1, index_of_char),
                                       (index_of_row + 1, index_of_char + 1)
                                       ]
                    for item in chars_to_change:
                        if garden[item[0]][item[1]] != '*':
                            garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]]) + 1)
                elif position == ('center', 'right'):
                    chars_to_change = [(index_of_row - 1, index_of_char - 1),
                                       (index_of_row - 1, index_of_char),
                                        (index_of_row, index_of_char - 1),
                                        (index_of_row + 1, index_of_char - 1),
                                       (index_of_row + 1, index_of_char),
                                       ]
                    for item in chars_to_change:
                        if garden[item[0]][item[1]] != '*':
                            garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]]) + 1)
                elif position == ('bottom', 'left'):
                     chars_to_change = [ (index_of_row - 1, index_of_char),
                                        (index_of_row - 1, index_of_char + 1),
                                        (index_of_row, index_of_char + 1),
                                        ]

                     if len(row) == 1:
                         chars_to_change.pop()
                         chars_to_change.pop()

                     for item in chars_to_change:
                         if garden[item[0]][item[1]] != '*':
                             garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]]) + 1)
                elif position == ('bottom', 'center'):
                    chars_to_change = [(index_of_row - 1, index_of_char - 1),
                                       (index_of_row - 1, index_of_char),
                                       (index_of_row - 1, index_of_char + 1),
                                       (index_of_row, index_of_char - 1),
                                       (index_of_row, index_of_char + 1)
                                       ]
                    for item in chars_to_change:
                        if garden[item[0]][item[1]] != '*':
                            garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]]) + 1)
                elif position == ('bottom', 'right'):
                    chars_to_change = [(index_of_row - 1, index_of_char - 1),
                                       (index_of_row - 1, index_of_char),
                                       (index_of_row, index_of_char - 1),
                                       ]
                    for item in chars_to_change:
                        if garden[item[0]][item[1]] != '*':
                            garden[item[0]][item[1]] = str(int(garden[item[0]][item[1]]) + 1)

    for index_of_rows, row in enumerate(garden):
        new_row = list(row)
        for index_of_char, char in enumerate(new_row):
            if new_row[index_of_char] == '0':
                new_row[index_of_char] = ' '
        garden[index_of_rows] = new_row

    for index  in range (len(garden)):
        garden[index] = ''.join(garden[index])
    return (garden)

# print(annotate([" ", "*", " ", "*", " "]))
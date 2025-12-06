OPERATIONS = ('plus', 'minus', 'multiplied', 'divided')
NUMBERS = '1 2 3 4 5 6 7 8 9 -'
NUMBERS_list = NUMBERS.split()
def answer (text):
    text = text.strip('?')
    answer:int = 0
    words = text.split()
    operation:str = ''
    for item in words:
        if (item[0] in NUMBERS_list) and (answer == 0):
            answer += int(item)
            continue
        if item in OPERATIONS:
            operation = item
            continue
        if (item[0] in NUMBERS_list) and (len(operation) != 0) and (answer != 0):
            if operation == 'plus':
                answer += int(item)
                operation = ''
                continue
            if operation == 'minus':
                answer -= int(item)
                operation = ''
                continue
            if operation == 'multiplied':
                answer *= int(item)
                operation = ''
                continue
            if operation == 'divided':
                answer //= int(item)
                operation = ''
                continue
        if (item == words[-1]) and (operation == '') and (answer == 0):
            return int(item)

        if item not in (OPERATIONS and NUMBERS_list):
            continue

    return answer
print(answer("What is 33 divided by -3?"))
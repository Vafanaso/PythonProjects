def is_valid(isbn):
    ind = 10
    result = 0
    numbers:list[str] = []
    for letter in isbn:
        if letter == '-':
            continue
        numbers.append(letter)
    if  len(numbers) != 10:
        return False
    for parts in numbers:
        if parts == 'X' and ind == 1:
            result += 10 * ind
            ind -= 1
            continue
        if (parts not in ('0','1','2','3','4','5','6','7','8','9','X')) or (parts == 'X' and ind != 1):
            return False
        result += int(parts) * ind
        ind -= 1
    if result % 11 == 0:
        return True
    return False
print (is_valid("3-598-2X507-9"))

def is_isogram(string):
    letters:list[str] = []
    for letter in string.lower():
        if letter in ['-',' ']: continue
        if letter not in letters:letters.append(letter)
        else: return False
    return True
print(is_isogram("Emily Jung Schwartzkopf"))
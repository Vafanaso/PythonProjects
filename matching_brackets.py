ALPHABETH = 'abcdefghijklmnopqrstuvwxyz'

def is_paired(input_string):
    brack:list[str] = []
    brackets = input_string.strip(ALPHABETH + ALPHABETH.upper())
    for items in brackets:
        if items not in "{}[]()":
            continue
        brack.append(items)
    new_stack = []
    if brack.count('{') != brack.count('}'):
        return False
    if brack.count('[') != brack.count(']'):
        return False
    if brack.count('(') != brack.count(')'):
        return False

    for index in range (len(brack)):
        if brack[index] in '([{':
            new_stack.append(brack[index])
            continue
        if (brack[index] == ')') and new_stack != [] and new_stack[-1] == '(':
            new_stack.pop()
        elif (brack[index] == ')') and new_stack == []:
            return False
        if (brack[index] == '}') and new_stack != [] and new_stack[-1] == '{':
            new_stack.pop()
        elif (brack[index] == '}') and new_stack == []:
            return False
        if (brack[index] == ']') and new_stack != [] and  new_stack[-1] == '[':
            new_stack.pop()
        elif (brack[index] == ']') and new_stack == []:
            return False
    if new_stack == []:
        return True
    return False

print(is_paired("]["))
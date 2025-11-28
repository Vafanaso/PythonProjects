PLAIN = 'abcdefghijklmnopqrstuvwxyz'
def encode(plain_text):
    result:list[str] =[]
    unused_count = 0
    for index,item in enumerate(plain_text):
        if index >=5 and (index - unused_count) % 5 ==0 and item == ' ':
            result.append(' ')
            continue
        if index >=5 and (index - unused_count) % 5 ==0:
            result.append(' ')
        if item in '0123456789':
            result.append(item)
        elif item.lower() in PLAIN:
            result.append(PLAIN[-1* (PLAIN.find(item.lower()) +1)])
        else:
            unused_count += 1
            continue
    return "".join(result)
def decode(ciphered_text):
    cipher = PLAIN[::-1]
    result: list[str] = []
    for item in ciphered_text:
        if item == ' ':
            continue
        if item in '0123456789':
            result.append(item)
        if item.lower() in cipher:
            result.append(cipher[-1 * (cipher.find(item.lower()) + 1)])
        else:continue
    return "".join(result)


print(encode("Testing,1 2 3, testing."))
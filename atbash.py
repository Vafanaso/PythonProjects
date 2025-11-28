PLAIN = 'abcdefghijklmnopqrstuvwxyz'
def encode(plain_text):
    result:list[str] = []
    plain_text = plain_text.replace(' ', '').replace(',', '')
    for index, item in enumerate(plain_text):
        if (index >= 5) and (index % 5 == 0) and (item is not plain_text[-1]):
            result.append(' ')

        if item in '1234567890':
            result.append(item)
        if item.lower() in PLAIN:
            result.append(PLAIN[(-1 * (PLAIN.index(item.lower()) + 1))])
    return ''.join(result)
def decode(ciphered_text ):
    result:list[str] = []
    nilap = PLAIN[::-1]
    ciphered_text = ciphered_text.replace(' ', '')
    for index, item in enumerate(ciphered_text):
        if item in '1234567890':
            result.append(item)
        if item.lower() in nilap:
            result.append(nilap[-1 * (nilap.index(item) + 1)])
    return ''.join(result)



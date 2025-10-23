def rotate(text, key):
    """Encryption based on the alphabetic shift

    :param text: str - the given test that needs to be encrypted
    :param key: int - the number of shift in alphabet
    :return end : str - the result of encryption
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res:list[str] = []
    if key  >= 26:
        key %= 26
    for letters in text:
        if letters not in alphabet and letters not in alphabet.upper():
            res.append(letters)
            continue
        if key + alphabet.find(letters.lower()) >= 26:
            if letters.isupper():
                res.append(alphabet[key - (26 - alphabet.find(letters.lower()))].upper())
                continue
            res.append(alphabet[key - (26 - alphabet.find(letters))])
        else:
            if letters.isupper():
                res.append(alphabet[alphabet.find(letters.lower()) + key].upper())
                continue
            res.append(alphabet[alphabet.find(letters) + key])
    end = ''.join(res)
    return end
print (rotate("The quick brown fox jumps over the lazy dog.",13))


def is_pangram(sentence):
    alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    """Provide functionality to check if a given sentence is a pangram or not.

A pangram is a sentence that contains every letter of the English alphabet
at least once.

Functions:
    - is_pangram(sentence): Determine if the given sentence is a pangram.
        param sentance: str - sentecne that will be checked
        return: bool - True if is a panagram and false if not
    """
    for i in sentence.lower():
        if i in alphabeth:
            alphabeth.remove(i)
        if not alphabeth:
            return True
    return False

print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"))

"""
Introduction
Your parents have challenged you and your sibling to a game of two-on-two basketball. Confident they'll win, they let you score the first couple of points, but then start taking over the game. Needing a little boost, you start speaking in Pig Latin, which is a made-up children's language that's difficult for non-children to understand. This will give you the edge to prevail over your parents!

Instructions
Your task is to translate text from English to Pig Latin. The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word. These rules look at each word's use of vowels and consonants:

vowels: the letters a, e, i, o, and u
consonants: the other 21 letters of the English alphabet
Rule 1
If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.

For example:

"apple" -> "appleay" (starts with vowel)
"xray" -> "xrayay" (starts with "xr")
"yttria" -> "yttriaay" (starts with "yt")
Rule 2
If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.

For example:

"pig" -> "igp" -> "igpay" (starts with single consonant)
"chair" -> "airch" -> "airchay" (starts with multiple consonants)
"thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
Rule 3
If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.

For example:

"quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
"square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")
Rule 4
If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

Some examples:

"my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
"rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")
"""
VOWELS = ['a','e','i','o','u']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                           'x', 'y', 'z']
CONSONANTS_WITHOUT_Y = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                           'x', 'z']


def translate(text:str)->str|None:
    """
    Translating the normal human languae into kids sick and disgusting pig form which is a joke to sanity

    param text: str - the text that is gonng too be translated
    return: str - Pig joke
    """
    words = text.split()
    new_words:list[str]=[]
    for word in words:
        vowels:str = ""

        word = word[1:] if word.startswith("y") and word.startswith("yt") else word

        if word.startswith("y") and not word.startswith('yt'):
            vowels += 'y'
            word = word[1:]
        if word[0] in VOWELS or word.startswith("yt") or word.startswith("xr"):
            word += vowels
            word += "ay"
            new_words.append(word)
            continue
        if word[0] in CONSONANTS:
            for letter in word:
                if letter in CONSONANTS_WITHOUT_Y:
                    vowels += letter
                else:
                    if word.startswith(vowels[:-1]+'qu'):
                        vowels += 'u'
                    break

            word = (word +vowels + "ay")[len(vowels):]
        new_words.append(word)
    return " ".join(new_words)

print(translate("yttria"))
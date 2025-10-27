def color_code(color):
    colors_list = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]
    return colors_list.index(color)


def colors():
    return [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]
def value(colors):
    num = ''
    for item in colors[:2:]:
        num +=str(color_code(item))
    return int(num)

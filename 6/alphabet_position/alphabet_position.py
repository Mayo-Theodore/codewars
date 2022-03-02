def alphabet_position(sentence):
    sentence_lower = sentence.lower()
    converter = ""
    check_word = 0
    positions = {
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6",
        "g": "7",
        "h": "8",
        "i": "9",
        "j": "10",
        "k": "11",
        "l": "12",
        "m": "13",
        "n": "14",
        "o": "15",
        "p": "16",
        "q": "17",
        "r": "18",
        "s": "19",
        "t": "20",
        "u": "21",
        "v": "22",
        "w": "23",
        "x": "24",
        "y": "25",
        "z": "26",
    }

    for letter in sentence_lower:
        if letter.isalpha():
            converter += positions[letter] + " " 
    return converter[:-1]

def all_letters(sentence):
    for character in sentence:
        if character.isalpha():
            return True
        else: 
            return False


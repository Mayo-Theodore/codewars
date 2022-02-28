def capital(word):
    return word.lower()

def brackets(word):
    bracket_list = []
    for x in word:
        bracket_list.append("(")
    return "".join(bracket_list)
        
def duplicate_chars(word):
    converter = []
    word_lower = word.lower()
    for x in word_lower:
        if word_lower.count(x) == 1:
            converter.append("(")
        else:
            converter.append(")")
    return "".join(converter)
            
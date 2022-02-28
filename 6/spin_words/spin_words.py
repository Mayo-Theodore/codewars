def word_split(sentence):
    return sentence.split()

def word_count(sentence):
    words = sentence.split()
    word_list = []
    for word in words:
        word_list.append(len(word))
    return word_list

def spin_a_word(sentence):
    return sentence[::-1]

def spin_words(sentence):
    words = sentence.split()
    word_list = []
    for word in words:
        if len(word) <= 4:
            word_list.append(word)
        else:
            word_list.append(word[::-1])
    return " ".join(word_list)
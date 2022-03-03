def to_camel_case(string):
    if string == "":
        return ""
    string_list = list(string)
    new = string_list
    indexes = [index for index, element in enumerate(new) if element == "-"]
    under_indexes = [index for index, element in enumerate(new) if element == "_"]
    print(under_indexes)
    if indexes:
        for i in indexes:
            new[i] = ""
            new[i + 1] = new[i + 1].upper()
        if string_list[0].isupper():
            new[0] = new[0].upper()
            return "".join(new)
        else:
            return "".join(new)

    if under_indexes:
        for i in under_indexes:
            new[i] = ""
            new[i + 1] = new[i + 1].upper()
        if string_list[0].isupper():
            new[0] = new[0].upper()
            return "".join(new)
        else:
            return "".join(new)
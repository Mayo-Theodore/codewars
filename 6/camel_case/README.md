Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

Edge cases
Empty string? --> Return empty string
Numbers in string? --> Ignore numbers

def to_camel_case(string):
    if string == "":
        return ""
    string_list = list(string)
    new = string_list
    hyphen_indexes = [index for index, element in enumerate(new) if element == "-"]
    under_indexes = [index for index, element in enumerate(new) if element == "_"]
    print(hyphen_indexes)
    print(under_indexes)

    for i in hyphen_indexes:
        new[i] = ""
        new[i + 1] = new[i + 1].upper()
        if string_list[0].isupper():
            new[0] = new[0].upper()
            return "".join(new)
        else:
            return "".join(new)

    for i in under_indexes:
        new[i] = ""
        new[i + 1] = new[i + 1].upper()
        if string_list[0].isupper():
            new[0] = new[0].upper()
            return "".join(new)
        else:
            return "".join(new)
                

    
    # for x in new:
    #     if x == "_":
    #         under_index = new.index(x)
    #         new[under_index] = ""
    #         new[under_index + 1] = new[under_index + 1].upper()
    #         return "".join(new)

            



    # if under_indexes:
    #     for i in under_indexes:
    #         new[i] = ""
    #         new[i + 1] = new[i + 1].upper()
    #     if string_list[0].isupper():
    #         new[0] = new[0].upper()
    #         return "".join(new)
    #     else:
    #         return "".join(new)
        
        
def unique(input):
    array = []
    i = 1
    if not input or input == "":
        return []

    while i < len(input):
        if input[i] != input[i - 1]:
            array.append(input[i])
        i += 1
    array.insert(0, input[0])
    return array
        
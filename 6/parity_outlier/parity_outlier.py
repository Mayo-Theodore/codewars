def an_integer(list):
    return list.pop()

def integer_type(list):
    even = []
    odd = []
    for x in list:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    if len(odd) > len(even):
        return 'Odd'
    else:
        return 'Even'

def outlier(list):
    even = []
    odd = []
    for x in list:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    if len(even) > len(odd):
        for x in list:
            if x not in even:
                return x
    else:
        for x in list:
            if x not in odd:
                return x

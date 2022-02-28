def digital_root(n):
    list_int = [int(i) for i in str(n)]
    if len(str(sum(list_int))) == 1:
        return sum(list_int)
    else:
        return digital_root(sum(list_int))


def digit_check(n):
    string_digit = str(n)
    digit_length = len(string_digit)
    if digit_length < 2:
        return "Please enter a minimum of 2 digits"

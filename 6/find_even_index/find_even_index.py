from turtle import left


def find_even_index(values):
    left_total = 0
    right_total = 0

    if sum(values[1::]) == 0:
        return 0

    for i in values:
            left_total = sum(values[::i+1])
            right_total = sum(values[i+1::])
            print(left_total)
            print(right_total)

            if left_total == right_total:
                return i
    return -1
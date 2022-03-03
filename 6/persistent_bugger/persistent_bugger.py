def number_of_digits(n):
    return len(str(n))

def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        value = 1
        for i in n:
            value *= int(i)
        n = str(value)
        count += 1
    return count 


# def persistence_second(n):
#     if persistence(n) > 9:
#         persistence(persistence(n))
#     elif persistence(persistence(n)) > 9:
#            persistence(persistence(persistence(n)))
#     elif persistence(persistence(persistence(n))) > 9:
#         persistence(persistence(persistence(persistence(n))))
#     return persistence(persistence(persistence(persistence(n))))


  


def number_of_digits(n):
    return len(str(n))

def persistence(n):
    value = 1
    for i in range(len(str(n))):
        value *= int(str(n)[i])
    if value > 9:
        persistence(value)
        return persistence(value)



# def persistence_second(n):
#     if persistence(n) > 9:
#         persistence(persistence(n))
#     elif persistence(persistence(n)) > 9:
#            persistence(persistence(persistence(n)))
#     elif persistence(persistence(persistence(n))) > 9:
#         persistence(persistence(persistence(persistence(n))))
#     return persistence(persistence(persistence(persistence(n))))


  


# If you can't sleep, just count sheep!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

# def count_sheep(n):
#     sheep_list = [x for x in range(1, n + 1)]
#     total_sheep = []
#     for i in sheep_list:
#         total_sheep.append("{} sheep...".format(i))
#     return "".join(total_sheep)

def count_sheep(n):
    return ''.join("{} sheep...".format(i) for i in range(1,n+1))

print(count_sheep(3))

# name = 'World'
# program = 'Python'
# print("hello {}".format(name))
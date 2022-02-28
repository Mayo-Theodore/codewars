def convert_to_binary(n):
    binary = int(bin(n)[2:])
    return binary

def count_binary(n):
    binary = bin(n)[2:]
    return binary.count('1')
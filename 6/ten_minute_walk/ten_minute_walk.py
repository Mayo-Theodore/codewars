def is_ten_mins(walk):
    return len(walk)

def starting_point(walk):
    end_location = 0
    if len(walk) == 10:
        starting_location = 0
        for direction in walk:
            if direction == 'n':
                end_location += 1
            elif direction == 's':
                end_location -= 1
            elif direction == 'e':
                end_location += 2
            elif direction == 'w':
                end_location -= 2
    else:
        return False
    if end_location == starting_location:
        return True
    else:
        return False



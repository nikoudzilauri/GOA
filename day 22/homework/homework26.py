def digit(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return int(string[i])
    return None
# სწორია?

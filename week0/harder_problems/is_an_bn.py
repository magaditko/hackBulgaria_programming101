def is_an_bn(word):
    middle = len(word) // 2
    a_side = word[:middle] == 'a' * middle
    b_side = word[middle:]

    if a_side == "a" * middle and b_side == "b" * middle:
        return True
    else:
        return False

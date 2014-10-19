def is_an_bn(word):
    times = len(word) // 2
    a_side = word[:len(word) // 2]
    b_side = word[len(word) // 2:]

    if a_side == "a" * times and b_side == "b" * times:
        return True
    else:
        return False

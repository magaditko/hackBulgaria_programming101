def is_an_bn(word):
    times = len(word) // 2
    a_side = word[:len(word) // 2]
    b_side = word[len(word) // 2:]

    if a_side == "a" * times and b_side == "b" * times:
        return True
    else:
        return False

print(is_an_bn(""))
print(is_an_bn("rado"))
print(is_an_bn("aaabb"))
print(is_an_bn("aaabbb"))
print(is_an_bn("aabbaabb"))
print(is_an_bn("bbbaaa"))
print(is_an_bn("aaaaabbbbb"))
print(is_an_bn(""))

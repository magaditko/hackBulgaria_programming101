def sort_fractions(fractions):
    values = []
    result = []
    for fraction in fractions:
        if isinstance(fraction[0], int) and isinstance(fraction[1], int):
            value = fraction[0] / fraction[1]
            values.append([value, fraction])
        else:
            continue
    values.sort()
    for item in values:
        result.append(item[1])
    return result

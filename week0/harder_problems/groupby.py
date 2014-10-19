def groupby(func, seq):
    result = {}
    for number in seq:
        if func(number) not in result.keys():
            result[func(number)] = [number]
        else:
            result[func(number)].append(number)
    return result

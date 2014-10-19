def count_words(arr):
    result = {}
    for item in arr:
        if item in result.keys():
            result[item] += 1
        elif not item.isspace() and not item == '':
            result[item] = 1
    return result

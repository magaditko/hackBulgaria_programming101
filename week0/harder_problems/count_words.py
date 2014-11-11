def count_words(array):
    result = {}
    for item in array:
        if not item.isspace() and not item == '':
            result[item] = array.count(item)
    return result

def prepare_meal(number):
    n = 1
    largest_div = 0
    result = ""
    while (3 ** n) <= number:
        if number % (3 ** n) == 0:
            largest_div = n
        n += 1
    if largest_div != 0 and number % 5 == 0:
        result = "spam " * largest_div
        result += "and eggs"
    elif number % 5 == 0:
        result = "egg"
    else:
        result = "spam " * largest_div
    return result

def main():
    print(prepare_meal(15))
    
if __name__ == '__main__':
    main()

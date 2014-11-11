import sys
sys.path.insert(0, '../simple_problems/')

from is_prime import is_prime


def goldbach(even_integer):
    first_addend, second_addend = even_integer // 2
    result = []
    while second_addend <= even_integer:
        if is_prime(first_addend) and is_prime(second_addend):
            result.append((first_addend, second_addend))
        first_addend += 1
        second_addend -= 1
    return result

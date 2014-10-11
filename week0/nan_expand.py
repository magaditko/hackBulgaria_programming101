def nan_expand(times):
    if times == 0:
        return ""
    return "Not a " * times + "NaN"

def main():
    print(nan_expand(2))

if __name__ == '__main__':
    main()

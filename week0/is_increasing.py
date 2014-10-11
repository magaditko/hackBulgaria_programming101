def is_increasing(seq):
    result = True
    for number in range(len(seq) - 1):
        if seq[number] >= seq[number + 1]:
            result = False
    return result

def main():
    print(is_increasing([1,2,3,4,5]))
    
if __name__ == '__main__':
    main()

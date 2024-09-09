
def count(s):
    if s == "":
        return 0
    else:
        return 1 + count(s[1:])
    return n

def main():
    print(count('cat'))
    print(count('catastrophe'))
    print(count(''))

if __name__ == '__main__':
    main()

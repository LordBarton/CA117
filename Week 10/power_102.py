
def power(n, m, total=1):
    if m == 0:
        return total
    return power(n, m - 1, total * n)

def main():
    print(power(2,3))
    print(power(4,4))
    print(power(2,32))
    print(power(10,3))
    print(power(8,0))

if __name__ == '__main__':
    main()

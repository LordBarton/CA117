
def reverse(lst):
    if lst == []:
        return []
    return [lst[-1]] + reverse(lst[:-1])

def main():
    print(reverse([1,2,3]))
    print(reverse([3,4,5,6]))
    print(reverse([1,2]))

if __name__ == '__main__':
    main()

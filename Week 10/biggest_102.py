
def biggest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_big = biggest(lst[1:])
        return lst[0] if lst[0] > sub_big else sub_big
def main():
    print(biggest([6,5,1,3,4]))
    print(biggest([6,5,11,3,4]))
    print(biggest([6,15,11,13,14]))
    print(biggest([6,15,11,13,4]))

if __name__ == '__main__':
    main()

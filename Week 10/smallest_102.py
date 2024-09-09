def smallest(l, smallvalue=None):
    if smallvalue == None:
        smallvalue = l[0]
    for item in l:
        if item < smallvalue:
            return smallest(l, item)
    return smallvalue

def main():
    print(smallest([6,5,1,3,4]))
    print(smallest([6,5,11,3,4]))
    print(smallest([6,15,11,13,14]))
    print(smallest([6,15,11,13,4]))

if __name__ == '__main__':
    main()

def main():
    t = int(input())
    while t>0:
        t -= 1
        n = input()
        tich = 1
        for i in n:
            if(i != '0'):
                tich *= ord(i) - ord('0') #chuyển str -> int

        print(tich)
main()
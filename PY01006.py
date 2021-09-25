def main():
    t = int(input())
    while(t>0):
        t -= 1
        s = input()
        check = True
        for i in s:
            if i != '4' and i != '7':
                check = False
                break
        if check == True:
            print("YES")
        else:
            print("NO")
main()

def thuan_nghich(n):
    if n < 11:
        return False
    s = str(n)
    s2 = s[::-1]
    if s != s2:
        return False
    return True

def main():
    t = int(input())
    while t>0:
        t -= 1
        n = int(input())
        sum = 0
        while n>0:
            sum += n%10
            n //= 10
        check = thuan_nghich(sum)
        if check:
            print("YES")
        else:
            print("NO")
main()
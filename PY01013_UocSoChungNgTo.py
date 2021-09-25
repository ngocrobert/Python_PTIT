from math import sqrt, gcd
def snt(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def main():
    t = int(input())
    while t>0:
        t -= 1
        a, b = input().split()
        a, b = int(a), int(b)
        ucln = gcd(a,b)
        sum = 0
        while ucln > 0:
            sum += ucln%10
            ucln//=10
        if snt(sum):
            print("YES")
        else:
            print("NO") 

        
        
main()
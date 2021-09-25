from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def main():
    t = int(input())
    while t>0:
        t -= 1
        sum = 0
        n = int(input())
        while n>0:
            sum += n%10
            n//=10
        check = isPrime(sum)
        if check:
            print("YES")
        else:
            print("NO")
main()

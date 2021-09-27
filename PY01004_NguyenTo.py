import math
def ucln(a,b):
    if b==0:
        return a
    return ucln(b,a%b)

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0 :
            return False
    return True
def main():
    t = int (input())
    while t>0:
        t -= 1
        n = int(input())
        dem = 1
        for i in range(2,n):
            if ucln(i,n)==1:
                dem += 1
        if (isPrime(dem)):
            print("YES")
        else:
            print("NO")
main()
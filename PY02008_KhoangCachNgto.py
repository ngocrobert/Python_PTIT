import math
def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

Prime = [2] #mảng lưu các số ngto
number = 2  
while (len(Prime)<1000):
    number += 1
    if isPrime(number):
        Prime.append(number)

n,x = input().split()
n,x = int(n), int(x)
for i in range(0,n): #lặp chạy mảng Prime
    print(x,end=' ')
    x += Prime[i]
print(x)
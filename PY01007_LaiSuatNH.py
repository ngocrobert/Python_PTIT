def main():
    t = int(input())
    while t>0:
       t -= 1
       n, x, m = input().split()
       n, x, m = float(n), float(x), float(m)
       time = 0
       while (n<m):
           time += 1
           n = n + n*(x/100)
       print(time)
main()

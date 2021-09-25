def main():
    n = 10
    a = [int(i) for i in input().split()]
    while (len(a) < n) :
        tmp = [int(i) for i in input().split()]
        a += tmp
    dem = 0
    a = [x%42 for x in a]
    for i in range(10):
        if a.index(a[i]) == i:
            dem += 1
    print(dem)
main()
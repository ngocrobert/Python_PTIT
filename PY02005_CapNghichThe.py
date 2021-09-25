def main():
    n = int(input())
    list_arr = list(map(int, input().split()))
    dem = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if list_arr[i] > list_arr[j]:
                dem += 1
            else:
                continue
    print(dem)

main()
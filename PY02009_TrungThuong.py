def main():
    t = int(input())
    while t>0:
        t -= 1
        arr = [0 for i in range(1001)] #mảng đếm số lần xuất hiện
        n = int(input())
        count = 0

        while count<n:
            k = int(input())
            arr[k] += 1
            count += 1
        res = 0
        Max = 0
        for i in range(1001):
            if arr[i] > Max:
                res = i
                Max = arr[i]
        print(res)
main()
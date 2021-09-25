n = int(input())

while n != 0:
    arr = []
    for i in range(n):
        num = input()
        arr.append(num.lstrip('0')) #loại 0 ở đầu
    arr = sorted(set(arr),key=int) #set => gtri trong mảng xuất hiện = 1; key = int => sorted theo int
    if (len(arr)) == 1:
        print("BANG NHAU")
    else:
        print(arr[0],arr[len(arr)-1])
    n = int(input())
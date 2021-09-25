t = int(input())
while t > 0:
    t-=1
    s = input()
    s = list(int(i) for i in s) #tạo 1 list mới, lưu từng gtri của s (hay tách s và lưu list)
    for i in range(len(s)-1, 0, -1): #duyệt từ cuối -> vị trí 1 với step = 1
        if s[i] >= 5:
            s[i-1] = s[i-1] + 1
        s[i] = 0
    # if s[0] == 10:
    #     s[0] = 0
    #     print(1, end='')
    for i in s:
        print(i,end='')
    print()
def main():
    t = int(input())
    while(t>0):
        t -= 1
        s = input()
        if s[0:2] == s[len(s)-2:]: #lấy từ vị trí 0->2 và (len-1)-1 -> len-1
            print("YES")
        else:
            print("NO")
main()
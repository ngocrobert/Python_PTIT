def LocPhat(s):
    if s[len(s)-2:] != '86':
        return False
    return True
t = int(input())
while t>0:
    t -= 1
    s = input()
    if LocPhat(s):
        print("YES")
    else:
        print("NO")

def check(s1,s2):
    for i in range(1,len(s1)):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i])-ord(s2[i-1])):
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    s = input()
    mark = check(s,s[::-1]) #truyền vào s & đảo của s
    if mark:
        print("YES")
    else:
        print("NO")

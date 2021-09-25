def check(s):
    n = len(s)
    if n%2==0 or n<=2 or s[0] == s[1]:
        return False
    for i in range(2,n,2):
        if s[0] != s[i]:
            return False
    return True
     
def main():
    t = int(input())
    while t>0:
        t -= 1
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
main()
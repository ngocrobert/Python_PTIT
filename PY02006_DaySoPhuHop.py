def sol(a,b,n):
    #sắp xếp lại 2 list
    a.sort()
    b.sort()
    for i in range(n):
        if b[i] < a[i]:
            return False
    return True

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if sol(a,b,n):
            print("YES")
        else :
            print("NO")
main()
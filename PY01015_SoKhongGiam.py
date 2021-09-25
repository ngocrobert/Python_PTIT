
def check(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True
def main():
    t = int(input())
    while t>0:
        t -= 1
        n = input()
        mark = check(n)
        
        if mark == True:
            print("YES")
        else:
            print("NO")
main()
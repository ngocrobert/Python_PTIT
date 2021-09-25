def main():
    s1 = input()
    s2 = input()
    p = int(input())
    if p == 1:
        print(s2 + s1)
    else:
        print(s1[:p-1] + s2 + s1[p-1:]) 
        # từ 0->p-1 + s2 + p-1->len(s1)-1
main()
n = int(input())
arr = list(int(i) for i in input().split()) #nhập list int
Min = 10**9
res = 0
for i in arr:
    count = 0
    for j in arr:
        count += abs(j-i)
    if count < Min:
        Min = count
        res = i
print(Min,res)
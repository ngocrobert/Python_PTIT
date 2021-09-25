s = input()
size = len(s)
for i in range(3,size,3):
    s = s[:size-i] + ',' + s[size-i:]
print(s)
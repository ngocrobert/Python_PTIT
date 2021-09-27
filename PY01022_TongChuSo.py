import math

def main():
    num = input()
    if len(num) == 1:
        print(1)
    else:
        dem = 0
        while(len(num)!=1):
            sum = 0
            for i in num:
                sum += ord(i) - ord('0')
            num = str(sum)
            dem += 1
        print(dem)
main()
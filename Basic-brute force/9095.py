num = int(input())

sum = 0

def par(i):
    if i == 1:
        return 1
    if i == 2:
        return 2
    if i == 3:
        return 4
    return par(i-1) + par(i-2) + par(i-3)


for i in range(num):
    n = int(input())
    sum = par(n)
    print(sum)
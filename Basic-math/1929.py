num = list(map(int, input().split()))
N = num[-1]
count = 0

sosu = [0]*(N+1)
for i in range(2,N+1):
    for j in range(1,N//i+1):
        sosu[i*j] += 1
            
for i in range(num[0],num[1]+1):
    if sosu[i] == 1:
        print(i)
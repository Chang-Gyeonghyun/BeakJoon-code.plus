T = int(input())

for i in range(T):
    M,N,x,y = map(int,input().split())
    valid = 0
    for j in range(N):
        if (j*M+x-y)%N == 0:
            print(j*M+x)
            valid = 1
            break
    if valid == 0:
        print("-1")
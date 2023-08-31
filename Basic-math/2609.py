A, B = list(map(int,input().split()))


if A > B:
    for i in range(1, B+1):
        if A%i == 0 and B%i == 0:
            yaksu = i
    i = 1
    while True:
        if (B*i) % A ==0 :
            baesu = B*i
            break
        i += 1
elif A < B:
    for i in range(1, A+1):
        if A%i == 0 and B%i == 0:
            yaksu = i
    i = 1
    while True:
        if (A*i) % B ==0 :
            baesu = A*i
            break
        i += 1
else:
    yaksu = A
    baesu = A

print(yaksu)
print(baesu)
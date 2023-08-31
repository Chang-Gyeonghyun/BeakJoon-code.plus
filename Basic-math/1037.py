N = int(input())
yaksu = list[N]
yaksu = list(map(int,input().split()))
yaksu.sort()
sum = yaksu[0] * yaksu[-1]
print(sum)
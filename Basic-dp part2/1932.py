N = int(input())
arr = [[] for _ in range(501)]
dp = [[0 for _ in range(501)] for _ in range(501)]

for i in range(N):
    temp = list(map(int, input().split()))
    arr[i+1] = temp

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j-1]

print(max(dp[N]))
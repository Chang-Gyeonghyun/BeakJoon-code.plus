N = int(input())
MOD = 10007
dp = [[0] * 10 for _ in range(N+1)]
dp[0] = [1] * 10

for i in range(1, N):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][k] for k in range(j+1)) % MOD

print(sum(dp[N-1]) % MOD)
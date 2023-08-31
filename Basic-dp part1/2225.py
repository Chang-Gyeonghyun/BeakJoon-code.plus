N, K = map(int, input().split())
dp = [[0] * (201) for _ in range(201)]

def answer(N, K):
    for j in range(N+1):
        dp[j][1] = 1
    for k in range(2, K+1):
        for i in range(N+1):
            for j in range(i+1):
                dp[i][k] = (dp[i][k] + dp[j][k-1]) % 1000000000

    return dp[N][K]

print(answer(N, K))
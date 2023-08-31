from collections import defaultdict
N = int(input())
count = 0
dp = defaultdict()
dp[1] = 1
dp[2] = 2
def DP(n):
    if n in dp.keys():
        return dp[n]
    dp[n] = DP(n-2) + DP(n-1)
    return dp[n]
print(DP(N)%10007)
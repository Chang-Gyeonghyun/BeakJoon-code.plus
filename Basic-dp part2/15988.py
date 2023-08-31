T = int(input())
dp = [0 for _ in range(1000001)]
MOD = 1000000009
stack = []
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(T):
    start = 4
    n = int(input())
    if stack:
        start = max(stack)
    for i in range(start,n+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD
    stack.append(n)
        
    print(dp[n])
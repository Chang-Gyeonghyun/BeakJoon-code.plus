from collections import defaultdict
N = int(input())
count = 0
dp = defaultdict()
dp[1] = 0 
def DP(n):
    if n in dp.keys():
        return dp[n]
    if (n%3==0) and (n%2==0):
        dp[n]=min(DP(n//3)+1, DP(n//2)+1)
    elif n%3==0:
        dp[n]=min(DP(n//3)+1, DP(n-1)+1)
    elif n%2==0:
        dp[n]=min(DP(n//2)+1, DP(n-1)+1)
    else:
        dp[n]=DP(n-1)+1
    return dp[n]
print(DP(N))
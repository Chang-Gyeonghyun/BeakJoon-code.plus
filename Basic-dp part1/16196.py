from collections import defaultdict, deque
import sys
N = int(input())
dp = [10000 for _ in range(N+1)]
arr = list(map(int, input().split()))
arr = deque(arr)
arr.appendleft(0)
dp[0] = 0

for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = min(dp[i], dp[i-k] + arr[k])
print(dp[i])
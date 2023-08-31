from collections import defaultdict, deque
import sys
N = int(input())
dp = [0 for _ in range(N+1)]
arr = list(map(int, input().split()))
arr = deque(arr)
arr.appendleft(0)

for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + arr[k])
print(dp[i])
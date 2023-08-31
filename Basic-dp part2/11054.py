n = int(input())
array = list(map(int, input().split()))

dp = [[1, 1] for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i - 1, -1):
        if array[i] > array[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

maximum = 0
for i in range(n):
    maximum = max(maximum, dp[i][0] + dp[i][1] - 1)  # 중복되는 i번째 원소를 빼줍니다.

print(maximum)
N = int(input())
arr = [0]  # 0번 인덱스는 사용하지 않으므로 더미 데이터 0을 추가
for _ in range(N):
    n = int(input())
    arr.append(n)

dp = [0] * (N+3)  # dp 배열 크기를 N+3으로 확장
dp[1] = arr[1]
if N>=2:
    dp[2] = arr[1] + arr[2]
if N>=3:
    dp[3] = max(arr[1] + arr[2], arr[1] + arr[3], arr[2] + arr[3])

for i in range(4, N+1):
    dp[i] = max(dp[i-2] + arr[i], arr[i] + arr[i-1] + dp[i-3], dp[i-1])

print(dp[N])
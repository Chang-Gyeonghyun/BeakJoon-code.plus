N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]  # dp[i][j]: i번째 집을 j색으로 칠했을 때의 최소 비용

for i in range(N):
    if i == 0:
        dp[i] = arr[i]
    else:
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])  # 현재 집을 빨강으로 칠했을 때의 최소 비용
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])  # 현재 집을 초록으로 칠했을 때의 최소 비용
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])  # 현재 집을 파랑으로 칠했을 때의 최소 비용

print(min(dp[N-1]))  # 마지막 집을 각 색상으로 칠한 경우 중에서 최소 비용을 선택
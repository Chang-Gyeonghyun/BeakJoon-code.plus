N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]  # dp[i][j]: i��° ���� j������ ĥ���� ���� �ּ� ���

for i in range(N):
    if i == 0:
        dp[i] = arr[i]
    else:
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])  # ���� ���� �������� ĥ���� ���� �ּ� ���
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])  # ���� ���� �ʷ����� ĥ���� ���� �ּ� ���
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])  # ���� ���� �Ķ����� ĥ���� ���� �ּ� ���

print(min(dp[N-1]))  # ������ ���� �� �������� ĥ�� ��� �߿��� �ּ� ����� ����
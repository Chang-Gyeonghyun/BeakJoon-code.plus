N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N  # �� ���ҷ� ������ �����ϴ� �κ� ������ ���̸� �����ϴ� �迭

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_length = max(dp)  # ���� �� �κ� ������ ����
idx = dp.index(max_length)  # ���� �� �κ� ������ ������ ������ �ε���

subsequence = [arr[idx]]  # ���� �� �κ� ������ ã�Ƴ���

for i in range(idx - 1, -1, -1):
    if arr[i] < arr[idx] and dp[i] == dp[idx] - 1:
        subsequence.append(arr[i])
        idx = i

subsequence.reverse()  # �������� ���������Ƿ� ���� ������� ������

print(max_length)
print(" ".join(map(str, subsequence)))
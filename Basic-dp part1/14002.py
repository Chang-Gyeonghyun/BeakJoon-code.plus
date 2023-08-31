N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N  # 각 원소로 끝나는 증가하는 부분 수열의 길이를 저장하는 배열

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_length = max(dp)  # 가장 긴 부분 수열의 길이
idx = dp.index(max_length)  # 가장 긴 부분 수열의 마지막 원소의 인덱스

subsequence = [arr[idx]]  # 가장 긴 부분 수열을 찾아나감

for i in range(idx - 1, -1, -1):
    if arr[i] < arr[idx] and dp[i] == dp[idx] - 1:
        subsequence.append(arr[i])
        idx = i

subsequence.reverse()  # 역순으로 저장했으므로 원래 순서대로 뒤집음

print(max_length)
print(" ".join(map(str, subsequence)))
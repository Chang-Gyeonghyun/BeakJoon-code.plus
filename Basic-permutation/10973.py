N = int(input())
arr = list(map(int, input().split()))

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1
    if i == -1:
        return []  # 이미 가장 작은 순열일 경우
    j = n - 1
    while arr[j] >= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = sorted(arr[i+1:],reverse=True)
    return arr

ans = next_permutation(arr)
if ans:
    print(" ".join(map(str, ans)))
else:
    print(-1)
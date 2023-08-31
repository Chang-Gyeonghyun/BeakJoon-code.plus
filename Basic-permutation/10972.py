N = int(input())
arr = list(map(int, input().split()))

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return []  # 이미 가장 큰 순열인 경우
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = sorted(arr[i+1:])
    return arr

ans = next_permutation(arr)
if ans:
    print(" ".join(map(str, ans)))
else:
    print(-1)
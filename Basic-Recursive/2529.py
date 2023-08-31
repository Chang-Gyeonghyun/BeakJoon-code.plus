import sys

k = int(input())
arr = list(input().split())

stack = []
maximum = -sys.maxsize
minimum = sys.maxsize

def dfs(idx):
    global maximum, minimum, stack
    
    if len(stack) == k + 1:
#개수가 다 찼을 경우 결과값을 업데이트 한다.
        temp = int("".join(map(str, stack)))
        maximum = max(maximum, temp)
        minimum = min(minimum, temp)
        return

    for i in range(10):
        if not stack:
            stack.append(i)
            dfs(idx + 1)
            stack.pop()
        elif arr[idx-1] == '<' and i > stack[-1] and i not in stack:
#현재 인덱스의 전 값이 비교할 부등호임. 그리고 이전 값과 비교하고 그 값이 중복되지 않도록 해야한다.
            stack.append(i)
            dfs(idx + 1)
            stack.pop()
        elif arr[idx-1] == '>' and i < stack[-1] and i not in stack:
            stack.append(i)
            dfs(idx + 1)
            stack.pop()

dfs(0)
print(str(maximum).zfill(len(arr)+1))
print(str(minimum).zfill(len(arr)+1))
import sys

k = int(input())
arr = list(input().split())

stack = []
maximum = -sys.maxsize
minimum = sys.maxsize

def dfs(idx):
    global maximum, minimum, stack
    
    if len(stack) == k + 1:
#������ �� á�� ��� ������� ������Ʈ �Ѵ�.
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
#���� �ε����� �� ���� ���� �ε�ȣ��. �׸��� ���� ���� ���ϰ� �� ���� �ߺ����� �ʵ��� �ؾ��Ѵ�.
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
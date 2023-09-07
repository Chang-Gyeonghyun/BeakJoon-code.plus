import collections
        
def bfs(col, row, num):
    count = 0
    group[col][row] = num
    q = collections.deque()
    q.append((col, row))
    while q:
        count += 1
        (x, y) = q.popleft()
        if x + 1 < N and arr[x+1][y] == '1' and group[x + 1][y] == 0:
            group[x + 1][y] = num
            q.append((x + 1, y))
        if 0 <= x - 1 and arr[x-1][y] == '1' and group[x - 1][y] == 0:
            group[x - 1][y] = num
            q.append((x - 1, y))
        if y + 1 < N and arr[x][y+1] == '1' and group[x][y + 1] == 0:
            group[x][y + 1] = num
            q.append((x, y + 1))
        if 0 <= y - 1 and arr[x][y-1] == '1' and group[x][y - 1] == 0:
            group[x][y - 1] = num
            q.append((x, y - 1))
    return count

N = int(input())
arr = [list(input()) for _ in range(N)]
group = [[0] * N for _ in range(N)]
result = []

num = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and group[i][j] == 0:
            result.append(bfs(i, j, num))
            num += 1

print(len(result))
for count in sorted(result):
    print(count)
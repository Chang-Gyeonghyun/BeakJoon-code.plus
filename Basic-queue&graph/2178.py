import collections

def bfs():
    count = 0
    visit[0][0] = True
    q = collections.deque()
    q.append((0, 0))
    while q:
        count += 1
        size = len(q)
        for _ in range(size):
            (x, y) = q.popleft()
            if (x, y) == (N - 1, M - 1):
                return count
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '1' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
print(bfs())
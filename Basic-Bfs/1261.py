import collections

def bfs():
    visit[0][0] = True
    q = collections.deque()
    q.append((0, 0, 0))
    while q:
        size = len(q)
        for _ in range(size):
            (x, y, time) = q.popleft()
            if (x, y) == (N - 1, M - 1):
                return time
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.appendleft((nx, ny, time))
                elif 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    arr[nx][ny] = 0
                    q.append((nx, ny, time+1))

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
print(bfs())

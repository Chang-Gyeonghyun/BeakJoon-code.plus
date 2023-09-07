import collections

M, N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

def bfs():
    q = collections.deque()
    count = -1
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                q.append((i,j))
    while q:
        count += 1
        
        size = len(q)
        for _ in range(size):
            (x, y) = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    tomato[nx][ny] = 1
                    q.append((nx, ny))
                                 
    for row in tomato:
        for col in row:
            if col == 0:
                return -1
    return count
                    
print(bfs())
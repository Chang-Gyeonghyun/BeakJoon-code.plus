import collections

K = int(input())
position = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]

def bfs(xstart, ystart, xend, yend, visit):
    q = collections.deque()
    q.append((xstart, ystart))
    count = -1
    while q:
        count += 1
        size = len(q)
        for _ in range(size):
            (x, y) = q.popleft()
            if (x, y) == (xend, yend):
                return count
            for dx, dy in position:
                nx, ny = x + dx, y + dy
                if 0 <= nx < I and 0 <= ny < I and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
    

for _ in range(K):
    I = int(input())
    visit = [[False] * I for _ in range(I)]
    xstart, ystart = map(int, input().split())
    xend, yend = map(int, input().split())
    print(bfs(xstart, ystart, xend, yend, visit))

    
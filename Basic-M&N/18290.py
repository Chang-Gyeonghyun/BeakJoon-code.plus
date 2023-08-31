dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(depth, start, v):
    global ans
    if depth == K:
        ans = max(ans, v)
        return
    if v + 10000 * (K-depth) < ans:
        return
    
    for i in range(start, N*M):
        r = i % N
        c = i // N
        if visit[r][c]:
            continue
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if visit[nr][nc] == 1:
                break
        else:
            visit[r][c] = 1
            dfs(depth+1, i+1, v+lst[r][c])
            visit[r][c] = 0

N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
ans = -1_000_000_000

dfs(0, 0, 0)
print(ans)
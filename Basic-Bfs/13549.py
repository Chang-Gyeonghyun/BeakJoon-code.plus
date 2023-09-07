import collections

N, K = map(int, input().split())
max_position = 2 * max(N, K) + 1  # 큐의 최대 크기를 계산합니다.
visit = [False] * max_position

def hide():
    q = collections.deque()
    q.append((N,0))
    visit[N] = True
    
    while q:
        size = len(q)
        for i in range(size):
            temp, time = q.popleft()

            if temp == K:
                return time
            if temp * 2 < max_position and not visit[temp * 2]:
                q.append((temp * 2,time))
                visit[temp * 2] = True

            if temp - 1 >= 0 and not visit[temp - 1]:
                q.append((temp - 1,time+1))
                visit[temp - 1] = True

            if temp + 1 < max_position and not visit[temp + 1]:
                q.append((temp + 1,time+1))
                visit[temp + 1] = True



print(hide())
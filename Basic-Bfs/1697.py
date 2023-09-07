import collections

N, K = map(int, input().split())
max_position = 2 * max(N, K) + 1  # ť�� �ִ� ũ�⸦ ����մϴ�.
visit = [False] * max_position

def hide():
    q = collections.deque()
    q.append(N)
    visit[N] = True
    count = 0
    
    while q:
        size = len(q)
        for i in range(size):
            temp = q.popleft()

            if temp == K:
                return count

            if temp - 1 >= 0 and not visit[temp - 1]:
                q.append(temp - 1)
                visit[temp - 1] = True

            if temp + 1 < max_position and not visit[temp + 1]:
                q.append(temp + 1)
                visit[temp + 1] = True

            if temp * 2 < max_position and not visit[temp * 2]:
                q.append(temp * 2)
                visit[temp * 2] = True

        count += 1

print(hide())
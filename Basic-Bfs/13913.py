import collections

N, K = map(int, input().split())
max_position = 2 * max(N, K) + 1  # 큐의 최대 크기를 계산합니다.
visit = [False] * max_position
check = [0] * max_position

def move(current,count):
    position = []
    temp = current
    for _ in range(count):
        position.append(temp)
        temp = check[temp]
    position.append(N)
    print(count)
    print(' '.join(map(str,position[::-1])))

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
                move(temp,count)
                return

            if temp - 1 >= 0 and not visit[temp - 1]:
                q.append(temp - 1)
                visit[temp - 1] = True
                check[temp - 1] = temp

            if temp + 1 < max_position and not visit[temp + 1]:
                q.append(temp + 1)
                visit[temp + 1] = True
                check[temp + 1] = temp

            if temp * 2 < max_position and not visit[temp * 2]:
                q.append(temp * 2)
                visit[temp * 2] = True
                check[temp * 2] = temp
        count += 1

hide()
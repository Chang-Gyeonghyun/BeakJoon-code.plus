import collections

S = int(input())
visit = [[False] * (S + 1) for _ in range(S + 1)]  # 화면에 i개, 클립보드에 j개 이모티콘 있는지 체크
q = collections.deque()
q.append((1, 0, 0))  # 화면에 1개 있는 상태에서 시작

while q:
    screen, clipboard, time = q.popleft()
    
    # 이모티콘 개수가 S개가 되면 최소 시간 출력
    if screen == S:
        print(time)
        break
    
    # 복사 연산
    if not visit[screen][screen]:
        q.append((screen, screen, time + 1))
        visit[screen][screen] = True
    
    # 붙여넣기 연산
    if clipboard > 0 and screen + clipboard <= S and not visit[screen + clipboard][clipboard]:
        q.append((screen + clipboard, clipboard, time + 1))
        visit[screen + clipboard][clipboard] = True
    
    # 삭제 연산
    if screen > 0 and not visit[screen - 1][clipboard]:
        q.append((screen - 1, clipboard, time + 1))
        visit[screen - 1][clipboard] = True

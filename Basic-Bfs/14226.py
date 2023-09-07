import collections

S = int(input())
visit = [[False] * (S + 1) for _ in range(S + 1)]  # ȭ�鿡 i��, Ŭ�����忡 j�� �̸�Ƽ�� �ִ��� üũ
q = collections.deque()
q.append((1, 0, 0))  # ȭ�鿡 1�� �ִ� ���¿��� ����

while q:
    screen, clipboard, time = q.popleft()
    
    # �̸�Ƽ�� ������ S���� �Ǹ� �ּ� �ð� ���
    if screen == S:
        print(time)
        break
    
    # ���� ����
    if not visit[screen][screen]:
        q.append((screen, screen, time + 1))
        visit[screen][screen] = True
    
    # �ٿ��ֱ� ����
    if clipboard > 0 and screen + clipboard <= S and not visit[screen + clipboard][clipboard]:
        q.append((screen + clipboard, clipboard, time + 1))
        visit[screen + clipboard][clipboard] = True
    
    # ���� ����
    if screen > 0 and not visit[screen - 1][clipboard]:
        q.append((screen - 1, clipboard, time + 1))
        visit[screen - 1][clipboard] = True

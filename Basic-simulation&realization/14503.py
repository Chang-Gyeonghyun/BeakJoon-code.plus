import sys

def dfs(x, y, v):
    global answer

    # �� ���̸� û��
    if graph[x][y] == 0:
        graph[x][y] = 2 # �湮 ó��
        answer += 1 # û�� ���� ī��Ʈ

    # �ݺ����� ���� 4���� Ȯ��
    for _ in range(4):
        nv = (v + 3) % 4 # ���� ���� + 3�� 4�� ���� �������� ���� ����
        nx = x + dx[nv]
        ny = y + dy[nv]

        # �̵� ��ġ�� �� ���̸� Ž��
        if graph[nx][ny] == 0:
            dfs(nx, ny, nv)
            return
        # ���� ���� ����
        v = nv

    # 4���� ��� Ž���ߴٸ�
    nv = (v + 2) % 4 # ������� + 2�� 4�� ���� �������� ���� ����
    nx = x + dx[nv]
    ny = y + dy[nv]

    # �̵� ��ġ�� ���̶�� ����
    if graph[nx][ny] == 1:
        return

    # �̵� ��ġ�� ���� �ƴ϶�� Ž��
    dfs(nx, ny, v)

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# d => 0,3,2,1 ������ ���ƾ���. ��/��/��/��
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
dfs(r, c, d)
print(answer)
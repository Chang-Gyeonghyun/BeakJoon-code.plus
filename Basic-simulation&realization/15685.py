import sys

input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# �巡�� Ŀ�� ������ ������ ����Ʈ
curves = []

for _ in range(n):
    x, y, d, g = map(int, input().split())
    curves.append((x, y, d, g))

# ��ǥ�� �巡�� Ŀ�꿡 ������ �Ǵ��� üũ���� ����Ʈ
check = [[0] * (101) for _ in range(101)]

for curve in curves:
    x, y, d, g = curve

    # �־��� g���뵿�� ������ ������� ��Ƶ� ����Ʈ
    move_list = [d]
    # ���� �����ϴ� x, y ��ǥ�� �湮üũ
    check[x][y] = 1

    # ���� ��ŭ �����̸鼭 ���� ������ ������Ʈ
    for i in range(g):
        tmp = []
        for j in range(len(move_list)):
            tmp.append((move_list[-j - 1] + 1) % 4)
        move_list.extend(tmp)

    # g ���� ��ŭ ������ ��, move_list�� �ִ� ������� Ȯ���ϸ鼭 ��ǥ�� ����ϰ�, check ó���� ���ݴϴ�.
    for i in move_list:
        nx = x + dx[i]
        ny = y + dy[i]
        check[nx][ny] = 1  # üũó��
        x, y = nx, ny  # ������ ���� ������ �������� ����

answer = 0
# 100,100 ��ǥ�� ���鼭 �� ��ǥ�� 1�� üũ�Ǿ� ���� ��, ������ ������, �Ʒ�, ������ �Ʒ� �밢���� 1�� üũ�Ǿ� ������ answer += 1 �� ���ݴϴ�.
for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i + 1][j] == 1 and check[i][j + 1] == 1 and check[i + 1][j + 1] == 1:
            answer += 1

print(answer)

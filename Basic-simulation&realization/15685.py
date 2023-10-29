import sys

input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 드래곤 커브 정보를 저장할 리스트
curves = []

for _ in range(n):
    x, y, d, g = map(int, input().split())
    curves.append((x, y, d, g))

# 좌표가 드래곤 커브에 포함이 되는지 체크해줄 리스트
check = [[0] * (101) for _ in range(101)]

for curve in curves:
    x, y, d, g = curve

    # 주어진 g세대동안 움직인 방향들을 담아둘 리스트
    move_list = [d]
    # 먼저 시작하는 x, y 좌표는 방문체크
    check[x][y] = 1

    # 세대 만큼 움직이면서 방향 정보를 업데이트
    for i in range(g):
        tmp = []
        for j in range(len(move_list)):
            tmp.append((move_list[-j - 1] + 1) % 4)
        move_list.extend(tmp)

    # g 세대 만큼 실행한 뒤, move_list에 있는 방향들을 확인하면서 좌표를 계산하고, check 처리를 해줍니다.
    for i in move_list:
        nx = x + dx[i]
        ny = y + dy[i]
        check[nx][ny] = 1  # 체크처리
        x, y = nx, ny  # 방향을 현재 움직인 방향으로 갱신

answer = 0
# 100,100 좌표를 돌면서 한 좌표가 1로 체크되어 있을 때, 나머지 오른쪽, 아래, 오른쪽 아래 대각선이 1로 체크되어 있으면 answer += 1 을 해줍니다.
for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i + 1][j] == 1 and check[i][j + 1] == 1 and check[i + 1][j + 1] == 1:
            answer += 1

print(answer)

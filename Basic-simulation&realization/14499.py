import sys

N, M, x, y, K = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [0] * 7  # 주사위 면의 인덱스가 1부터 시작하도록 7개로 초기화

# 주사위의 각 면의 인덱스를 지정해줍니다.
top, bottom, north, south, west, east = 1, 6, 5, 2, 3, 4

def roll_dice(command):
    global x, y, top, bottom, north, south, west, east
    new_x, new_y = x, y
    
    if command == 1 and y + 1 < M:
        new_y = y + 1
        top, bottom, west, east = west, east, bottom, top
        if maps[new_x][new_y] == 0:
            maps[new_x][new_y] = dice[bottom]
        else:
            dice[bottom] = maps[new_x][new_y]
            maps[new_x][new_y] = 0
        
        x, y = new_x, new_y
        print(dice[top])
    elif command == 2 and y - 1 >= 0:
        new_y = y - 1
        top, bottom, west, east = east, west, top, bottom
        if maps[new_x][new_y] == 0:
            maps[new_x][new_y] = dice[bottom]
        else:
            dice[bottom] = maps[new_x][new_y]
            maps[new_x][new_y] = 0
        
        x, y = new_x, new_y
        print(dice[top])
    elif command == 3 and x - 1 >= 0:
        new_x = x - 1
        top, bottom, north, south = south, north, top, bottom
        if maps[new_x][new_y] == 0:
            maps[new_x][new_y] = dice[bottom]
        else:
            dice[bottom] = maps[new_x][new_y]
            maps[new_x][new_y] = 0
        
        x, y = new_x, new_y
        print(dice[top])
    elif command == 4 and x + 1 < N:
        new_x = x + 1
        top, bottom, north, south = north, south, bottom, top
    
        if maps[new_x][new_y] == 0:
            maps[new_x][new_y] = dice[bottom]
        else:
            dice[bottom] = maps[new_x][new_y]
            maps[new_x][new_y] = 0
        
        x, y = new_x, new_y
        print(dice[top])

for command in commands:
    roll_dice(command)

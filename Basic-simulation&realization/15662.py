T = int(input())
arr = [list(map(int, input())) for _ in range(T)]
K = int(input())
rotation = []

def rotate(index, direction):
    if index < 0 or index >= T:
        return  # 인덱스가 범위를 벗어나면 종료
    
    visited[index] = True  # 방문한 톱니바퀴 기록

    # 왼쪽 톱니바퀴를 확인하고 회전
    if index > 0 and arr[index][6] != arr[index - 1][2] and not visited[index - 1]:
        rotate(index - 1, -direction)
    # 오른쪽 톱니바퀴를 확인하고 회전
    if index < T - 1 and arr[index][2] != arr[index + 1][6] and not visited[index + 1]:
        rotate(index + 1, -direction)
    
    # 현재 톱니바퀴 회전
    if direction == 1:
        arr[index].insert(0, arr[index].pop())
    else:
        arr[index].append(arr[index].pop(0))


for _ in range(K):
    index, direction = map(int, input().split())
    rotation.append((index - 1, direction))  # 인덱스를 0부터 시작하도록 조정

for index, direction in rotation:
    visited = [False] * T  # 매 회전마다 방문 여부 초기화
    rotate(index, direction)
    
count_s = 0
for i in range(T):
    if arr[i][0] == 1:
        count_s += 1
        
print(count_s)

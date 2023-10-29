## 16935 문제

크기가 N×M인 배열이 있을 때, 배열에 연산을 R번 적용하려고 한다. 연산은 총 6가지가 있다.

1번 연산은 배열을 상하 반전시키는 연산이다.

```
1 6 2 9 8 4 → 4 2 9 3 1 8
7 2 6 9 8 2 → 9 2 3 6 1 5
1 8 3 4 2 9 → 7 4 6 2 3 1
7 4 6 2 3 1 → 1 8 3 4 2 9
9 2 3 6 1 5 → 7 2 6 9 8 2
4 2 9 3 1 8 → 1 6 2 9 8 4
?  <배열>       <연산 결과>

```

2번 연산은 배열을 좌우 반전시키는 연산이다.

```
1 6 2 9 8 4 → 4 8 9 2 6 1
7 2 6 9 8 2 → 2 8 9 6 2 7
1 8 3 4 2 9 → 9 2 4 3 8 1
7 4 6 2 3 1 → 1 3 2 6 4 7
9 2 3 6 1 5 → 5 1 6 3 2 9
4 2 9 3 1 8 → 8 1 3 9 2 4
?  <배열>       <연산 결과>

```

3번 연산은 오른쪽으로 90도 회전시키는 연산이다.

```
1 6 2 9 8 4 → 4 9 7 1 7 1
7 2 6 9 8 2 → 2 2 4 8 2 6
1 8 3 4 2 9 → 9 3 6 3 6 2
7 4 6 2 3 1 → 3 6 2 4 9 9
9 2 3 6 1 5 → 1 1 3 2 8 8
4 2 9 3 1 8 → 8 5 1 9 2 4
?  <배열>       <연산 결과>
```

4번 연산은 왼쪽으로 90도 회전시키는 연산이다.

```
1 6 2 9 8 4 → 4 2 9 1 5 8
7 2 6 9 8 2 → 8 8 2 3 1 1
1 8 3 4 2 9 → 9 9 4 2 6 3
7 4 6 2 3 1 → 2 6 3 6 3 9
9 2 3 6 1 5 → 6 2 8 4 2 2
4 2 9 3 1 8 → 1 7 1 7 9 4
?  <배열>       <연산 결과>

```

5, 6번 연산을 수행하려면 배열을 크기가?N/2×M/2인 4개의 부분 배열로 나눠야 한다. 아래 그림은 크기가 6×8인 배열을 4개의 그룹으로 나눈 것이고, 1부터 4까지의 수로 나타냈다.

```
1 1 1 1 2 2 2 2
1 1 1 1 2 2 2 2
1 1 1 1 2 2 2 2
4 4 4 4 3 3 3 3
4 4 4 4 3 3 3 3
4 4 4 4 3 3 3 3
```

5번 연산은 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동시키는 연산이다.

```
3 2 6 3 1 2 9 7 → 2 1 3 8 3 2 6 3
9 7 8 2 1 4 5 3 → 1 3 2 8 9 7 8 2
5 9 2 1 9 6 1 8 → 4 5 1 9 5 9 2 1
2 1 3 8 6 3 9 2 → 6 3 9 2 1 2 9 7
1 3 2 8 7 9 2 1 → 7 9 2 1 1 4 5 3
4 5 1 9 8 2 1 3 → 8 2 1 3 9 6 1 8
?    <배열>            <연산 결과>

```

6번 연산은 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동시키는 연산이다.

```
3 2 6 3 1 2 9 7 → 1 2 9 7 6 3 9 2
9 7 8 2 1 4 5 3 → 1 4 5 3 7 9 2 1
5 9 2 1 9 6 1 8 → 9 6 1 8 8 2 1 3
2 1 3 8 6 3 9 2 → 3 2 6 3 2 1 3 8
1 3 2 8 7 9 2 1 → 9 7 8 2 1 3 2 8
4 5 1 9 8 2 1 3 → 5 9 2 1 4 5 1 9
?    <배열>            <연산 결과>

```

## 입력

첫째 줄에 배열의 크기 N, M과 수행해야 하는 연산의 수 R이 주어진다.

둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.

마지막 줄에는 수행해야 하는 연산이 주어진다. 연산은 공백으로 구분되어져 있고, 문제에서 설명한 연산 번호이며, 순서대로 적용시켜야 한다.

## 출력

입력으로 주어진 배열에 R개의 연산을 순서대로 수행한 결과를 출력한다.

## 제한

- 2 ≤ N, M ≤ 100
- 1 ≤ R ≤ 1,000
- N, M은 짝수
- 1 ≤ A?≤ 10
    
    ij
    
    8
    

## 예제 입력 1

```
6 8 1
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
1

```

## 예제 출력 1

```
4 5 1 9 8 2 1 3
1 3 2 8 7 9 2 1
2 1 3 8 6 3 9 2
5 9 2 1 9 6 1 8
9 7 8 2 1 4 5 3
3 2 6 3 1 2 9 7
```

### My code

```python
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))

def flip_horizontal(arr):
    return arr[::-1]

def flip_vertical(arr):
    for i in range(N):
        arr[i] = arr[i][::-1]
    return arr

def rotate_clockwise(arr, n, m):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = arr[n-1-j][i]
    return temp
    
def rotate_counterclockwise(arr, n, m):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = arr[j][m - 1 - i]
    return temp

def move_groups(arr):
    n, m = len(arr), len(arr[0])
    half_n, half_m = n // 2, m // 2
    new_arr = [[0] * m for _ in range(n)]

    for i in range(half_n):
        for j in range(half_m):
            new_arr[i][j] = arr[i + half_n][j]

    for i in range(half_n):
        for j in range(half_m, m):
            new_arr[i][j] = arr[i][j - half_m]

    for i in range(half_n, n):
        for j in range(half_m, m):
            new_arr[i][j] = arr[i - half_n][j]

    for i in range(half_n, n):
        for j in range(half_m):
            new_arr[i][j] = arr[i][j + half_m]

    return new_arr

def move_groups_reverse(arr):
    n, m = len(arr), len(arr[0])
    half_n, half_m = n // 2, m // 2
    new_arr = [[0] * m for _ in range(n)]

    for i in range(half_n):
        for j in range(half_m):
            new_arr[i][j] = arr[i][j+(half_m)]
    # 3 -> 2
    for i in range(half_n):
        for j in range(half_m, m):
            new_arr[i][j] = arr[i+(half_n)][j]
    # 4 -> 3
    for i in range(half_n, n):
        for j in range(half_m, m):
            new_arr[i][j] = arr[i][j-(half_m)]
    # 1 -> 4
    for i in range(half_n, n):
        for j in range(half_m):
            new_arr[i][j] = arr[i-(half_n)][j]

    return new_arr

def apply_operation(arr, op):
    
    if op == 1:
        return flip_horizontal(arr)
    elif op == 2:
        return flip_vertical(arr)
    elif op == 3:
        return rotate_clockwise(arr, len(arr), len(arr[0]))
    elif op == 4:
        return rotate_counterclockwise(arr, len(arr), len(arr[0]))
    elif op == 5:
        return move_groups(arr)  # 5번 연산
    elif op == 6:
        return move_groups_reverse(arr)  # 6번 연산

def apply_operations(arr, operations):
    for op in operations:
        arr = apply_operation(arr, op)
    return arr        
        
result = apply_operations(arr, operations)

for row in result:
    print(" ".join(map(str, row)))
```

## 16926 문제

크기가 N×M인 배열이 있을 때, 배열을 돌려보려고 한다. 배열은 다음과 같이 반시계 방향으로 돌려야 한다.

```
A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
   ↓                                       ↑
A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
   ↓         ↓                   ↑         ↑
A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
   ↓                                       ↑
A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
```

예를 들어, 아래와 같은 배열을 2번 회전시키면 다음과 같이 변하게 된다.

```
1 2 3 4       2 3 4 8       3 4 8 6
5 6 7 8       1 7 7 6       2 7 8 2
9 8 7 6   →   5 6 8 2   →   1 7 6 3
5 4 3 2       9 5 4 3       5 9 5 4
 <시작>         <회전1>        <회전2>
```

배열과 정수 R이 주어졌을 때, 배열을 R번 회전시킨 결과를 구해보자.

## 입력

첫째 줄에 배열의 크기 N, M과 수행해야 하는 회전의 수 R이 주어진다.

둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.

## 출력

입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.

## 제한

- 2 ≤ N, M ≤ 300
- 1 ≤ R ≤ 1,000
- min(N, M) mod?2 = 0
- 1 ≤ A?≤ 10
    
    ij
    
    8
    

## 예제 입력 1

```
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

```

## 예제 출력 1

```
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14
```

### First code

```python
N, M, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def circulate(row, col):
    temp = [[0 for _ in range(col)] for _ in range(row)]
    
    for nth in range(min(N,M)):
        for i in range(1 + nth, col - nth):
            temp[nth][i-1] = arr[nth][i]
        for i in range(nth, col-1-nth):
            temp[row-1-nth][i+1] = arr[row-1-nth][i]
        for i in range(nth, row-1-nth):
            temp[i+1][nth] = arr[i][nth]
        for i in range(1 + nth, row - nth):
            temp[i-1][col-1-nth] = arr[i][col-1-nth]
            
    return temp
for count in range(R):
    arr = circulate(N,M)
for rows in arr:
    print(" ".join(map(str,rows)))
```

위의 방법은 시간 초과가 떴습니다.

**`circulate`** 함수를 사용하여 배열을 회전시켰습니다. 이 함수는 반복문을 사용하여 배열을 한 번 회전할 때마다 모든 원소를 순회하면서 새로운 배열을 만들었습니다. 이는 각 회전 단계에서 모든 원소를 이동시키기 때문에 시간 복잡도가 높아집니다. 따라서 배열 크기와 회전 횟수가 커질수록 실행 시간이 길어질 것입니다. 

따라서 위의 문제를 해결한 코드입니다.

### Second Code

```python
N, M, R = map(int, input().split())  # N, M, R 값을 입력받습니다.
arr = [list(map(int, input().split())) for _ in range(N)]  # N개의 줄에 배열 A의 원소를 입력받아 2차원 리스트로 저장합니다.

def rotate_array(N, M, arr):
    # 회전 연산을 수행할 횟수를 최소로 줄이기 위해 배열을 그룹으로 나눕니다.
    num_layers = min(N, M) // 2
    rotated_arr = [row[:] for row in arr]  # 입력 배열을 복사한 배열을 만듭니다.

    for layer in range(num_layers):
        # 현재 그룹에서의 회전 연산 횟수를 계산합니다.
        num_rotations = R % (2 * (N + M - 4 * layer - 2))

        for _ in range(num_rotations):
            # 현재 그룹에서 한 번의 회전을 수행합니다.
            temp = rotated_arr[layer][layer]  # 현재 그룹의 왼쪽 위 원소를 임시로 저장합니다.

            # 왼쪽 변 회전: 왼쪽 열의 원소들을 한 칸씩 오른쪽으로 이동시킵니다.
            for i in range(layer, M - layer - 1):
                rotated_arr[layer][i] = rotated_arr[layer][i + 1]

            # 아래쪽 변 회전: 아래쪽 행의 원소들을 한 칸씩 위로 이동시킵니다.
            for i in range(layer, N - layer - 1):
                rotated_arr[i][M - layer - 1] = rotated_arr[i + 1][M - layer - 1]

            # 오른쪽 변 회전: 오른쪽 열의 원소들을 한 칸씩 왼쪽으로 이동시킵니다.
            for i in range(M - layer - 1, layer, -1):
                rotated_arr[N - layer - 1][i] = rotated_arr[N - layer - 1][i - 1]

            # 위쪽 변 회전: 위쪽 행의 원소들을 한 칸씩 아래로 이동시킵니다.
            for i in range(N - layer - 1, layer + 1, -1):
                rotated_arr[i][layer] = rotated_arr[i - 1][layer]

            # 회전을 마치고 임시로 저장한 값을 오른쪽 아래 원소에 대입합니다.
            rotated_arr[layer + 1][layer] = temp

    return rotated_arr  # 회전한 배열을 반환합니다.

result = rotate_array(N, M, arr)  # rotate_array 함수를 호출하여 배열을 회전시킵니다.

for row in result:  # 회전을 마친 배열을 출력합니다.
    print(" ".join(map(str, row)))  # 공백을 이용하여 한 줄에 출력합니다.
```

배열을 회전시키는 방식을 최적화하였습니다. 이 코드에서는 회전 연산을 수행할 때 실제로 원소들을 이동시키는 대신에 각 원소의 위치만을 변경합니다. 이렇게 하면 배열의 모든 원소를 순회하는 대신, 원소 위치의 변경만 수행하므로 시간 복잡도가 낮아집니다. 이 최적화는 반복문을 최소화하고, 배열의 크기나 회전 횟수에 관계없이 빠른 실행 속도를 제공합니다.

즉, 배열을 회전하는 방식을 최적화하여 더 빠른 실행 속도를 가집니다. 이전 코드에서는 매 회전마다 배열을 완전히 새로 만들고 이동시키는 방식을 사용하였기 때문에 큰 입력에 대해 시간 초과가 발생하는 것입니다.

## 14499 문제

크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 이 지도의 위에 주사위가 하나 놓여져 있으며, 주사위의 전개도는 아래와 같다. 지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다.

```
  2
4 1 3
  5
  6
```

주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

## 입력

첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20),?주사위를 놓은 곳의 좌표 x,?y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

## 출력

이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다.?만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

## 예제 입력 1

```
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

```

## 예제 출력 1

```
0
0
3
0
0
8
6
3
```

### My code

```python
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
```

### Solution

1. **`top`**, **`bottom`**, **`north`**, **`south`**, **`west`**, **`east`** 변수는 주사위의 각 면에 대한 인덱스를 나타냅니다. 주사위를 굴릴 때마다 이 변수들을 업데이트하여 주사위의 상태를 조작합니다.
2. **`roll_dice`** 함수는 주어진 명령에 따라 주사위를 굴리고, 윗 면에 쓰여 있는 값을 출력하는 역할을 합니다.
3. 주사위를 굴릴 때는 다음과 같이 주사위 면을 이동시킵니다.
    - 동쪽으로 굴리는 경우: **`top`**, **`bottom`**, **`west`**, **`east`** 값을 업데이트하고, 이동한 칸의 값이 0이면 주사위 바닥면에 값을 복사하고, 그렇지 않으면 이동한 칸의 값을 주사위 바닥면에 복사합니다.
    - 서쪽, 북쪽, 남쪽으로 굴리는 경우에도 마찬가지로 주사위를 굴립니다.
4. 주어진 명령 리스트를 순회하면서 **`roll_dice`** 함수를 호출하고, 주사위의 윗 면에 쓰여 있는 값을 출력합니다.

## 15662 문제

총 8개의 톱니를 가지고 있는 톱니바퀴 T개가 아래 그림과 같이 일렬로 놓여져 있다. 또,?톱니는 N극 또는 S극 중 하나를 나타내고 있다. 톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번,?..., 가장 오른쪽 톱니바퀴는 T번이다. 아래 그림은 T가 4인 경우이다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/1.png

이때, 톱니바퀴를 총 K번 회전시키려고 한다. 톱니바퀴의 회전은 한 칸을 기준으로 한다. 회전은 시계 방향과 반시계 방향이 있고, 아래 그림과 같이 회전한다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/2.png

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/3.png

톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와?회전시킬 방향을 결정해야 한다. 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다. 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 예를 들어, 아래와 같은 경우를 살펴보자.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/4.png

두 톱니바퀴의 맞닿은 부분은 초록색 점선으로 묶여있는 부분이다. 여기서, 3번 톱니바퀴를?반시계 방향으로 회전했다면, 4번 톱니바퀴는 시계 방향으로 회전하게 된다. 2번 톱니바퀴는 맞닿은 부분이 S극으로 서로 같기 때문에, 회전하지 않게 되고, 1번 톱니바퀴는 2번이 회전하지 않았기 때문에, 회전하지 않게 된다. 따라서, 아래 그림과 같은 모양을 만들게 된다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/5.png

위와 같은?상태에서 1번 톱니바퀴를 시계 방향으로 회전시키면, 2번 톱니바퀴가 반시계 방향으로 회전하게 되고, 2번이 회전하기 때문에, 3번도 동시에 시계 방향으로 회전하게 된다. 4번은 3번이 회전하지만, 맞닿은 극이 같기 때문에 회전하지 않는다. 따라서, 아래와 같은 상태가 된다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14891/6.png

톱니바퀴 T개의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 톱니바퀴의 개수 T (1 ≤ T ≤ 1,000)가 주어진다.

둘째 줄부터 T개의 줄에 톱니바퀴의 상태가 가장 왼쪽 톱니바퀴부터 순서대로 주어진다. 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.

다음 줄에는 회전 횟수 K(1 ≤ K ≤ 1,000)가 주어진다. 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

## 출력

총 K번 회전시킨 이후에 12시방향이?S극인 톱니바퀴의 개수를 출력한다.

## 예제 입력 1

```
4
10101111
01111101
11001110
00000010
2
3 -1
1 1

```

## 예제 출력 1

```
3
```

### My code

```python
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
```

### Solution

한 톱니바퀴가 움직인다면 그 톱니에 대해 다른 톱니도 맞물려서 움직여야 한다. 따라서 바로 생각난 것이 재귀이다.

다만 한 번 움직인 톱니로 다시 돌아가서 움직이게 하면 안되는 것이니까 visited배열로 방문 여부로 표시한다.

현재 톱니를 기준으로 왼쪽으로 그리고 오른쪽으로 재귀를 돌린다. 그리고 톱니 개수를 벗어난 경우 return을 통해 함수를 종료한다.

재귀를 마치고 나서는 자신의 톱니를 회전한다. 이때 톱니 회전의 방향을 살펴보고 왼쪽으로 한 칸 당기든지 오른쪽으로 당기는지 결정한다. 사실 deque를 통해 popleft(), appendleft()를 쓰면 더 시간 복잡도를 줄일 수 있긴 한데, 그것까지 구현하기는 귀찮아서 하지 않았다.

## 14503 문제

로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 방은??×?$N \times M$?크기의 직사각형으로 나타낼 수 있으며,?1×1$1 \times 1$?크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 방의 각 칸은 좌표?(?,?)$(r, c)$로 나타낼 수 있고, 가장 북쪽 줄의 가장 서쪽 칸의 좌표가?(0,0)$(0, 0)$, 가장 남쪽 줄의 가장 동쪽 칸의 좌표가?(??1,??1)$(N-1, M-1)$이다. 즉, 좌표?(?,?)$(r, c)$는 북쪽에서?(?+1)$(r+1)$번째에 있는 줄의 서쪽에서?(?+1)$(c+1)$번째 칸을 가리킨다. 처음에 빈 칸은 전부 청소되지 않은 상태이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변?$4$칸 중 청소되지 않은 빈 칸이 없는 경우,
    
    4
    
    1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변?$4$칸 중 청소되지 않은 빈 칸이 있는 경우,
    
    4
    
    1. 반시계 방향으로?$90^\circ$?회전한다.
        
        90?
        
    2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3. 1번으로 돌아간다.

## 입력

첫째 줄에 방의 크기??$N$과??$M$이 입력된다.?(3≤?,?≤50)$(3 \le N, M \le 50)$? 둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표?(?,?)$(r, c)$와 처음에 로봇 청소기가 바라보는 방향??$d$가 입력된다.??$d$가?0$0$인 경우 북쪽,?1$1$인 경우 동쪽,?2$2$인 경우 남쪽,?3$3$인 경우 서쪽을 바라보고 있는 것이다.

셋째 줄부터??$N$개의 줄에 각 장소의 상태를 나타내는??×?$N \times M$개의 값이 한 줄에??$M$개씩 입력된다.??$i$번째 줄의??$j$번째 값은 칸?(?,?)$(i, j)$의 상태를 나타내며, 이 값이?0$0$인 경우?(?,?)$(i, j)$가 청소되지 않은 빈 칸이고,?1$1$인 경우?(?,?)$(i, j)$에 벽이 있는 것이다. 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다. 로봇 청소기가 있는 칸은 항상 빈 칸이다.

## 출력

로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

## 예제 입력 1

```
3 3
1 1 0
1 1 1
1 0 1
1 1 1

```

## 예제 출력 1

```
1
```

### My code

```python
import sys

def dfs(x, y, v):
    global answer

    # 빈 곳이면 청소
    if graph[x][y] == 0:
        graph[x][y] = 2 # 방문 처리
        answer += 1 # 청소 구역 카운트

    # 반복문을 통해 4방향 확인
    for _ in range(4):
        nv = (v + 3) % 4 # 현재 방향 + 3을 4로 나눈 나머지가 왼쪽 방향
        nx = x + dx[nv]
        ny = y + dy[nv]

        # 이동 위치가 빈 곳이면 탐색
        if graph[nx][ny] == 0:
            dfs(nx, ny, nv)
            return
        # 현재 방향 변경
        v = nv

    # 4방향 모두 탐색했다면
    nv = (v + 2) % 4 # 현재방향 + 2를 4로 나눈 나머지가 후진 방향
    nx = x + dx[nv]
    ny = y + dy[nv]

    # 이동 위치가 벽이라면 리턴
    if graph[nx][ny] == 1:
        return

    # 이동 위치가 벽이 아니라면 탐색
    dfs(nx, ny, v)

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# d => 0,3,2,1 순서로 돌아야함. 북/서/남/동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
dfs(r, c, d)
print(answer)
```

## 15685 문제

드래곤 커브는 다음과 같은 세 가지 속성으로 이루어져 있으며, 이차원 좌표 평면 위에서 정의된다. 좌표 평면의 x축은?→ 방향, y축은?↓ 방향이다.

1. 시작 점
2. 시작 방향
3. 세대

0세대 드래곤 커브는 아래 그림과 같은 길이가 1인 선분이다. 아래 그림은 (0, 0)에서 시작하고, 시작 방향은 오른쪽인 0세대 드래곤 커브이다.

!http://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15685/1.png

1세대 드래곤 커브는 0세대 드래곤 커브를 끝 점을 기준으로 시계 방향으로 90도 회전시킨 다음 0세대 드래곤 커브의 끝 점에 붙인 것이다. 끝 점이란 시작 점에서 선분을 타고 이동했을 때, 가장 먼 거리에 있는 점을 의미한다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15685/2.png

2세대 드래곤 커브도 1세대를 만든 방법을 이용해서?만들 수 있다. (파란색 선분은 새로 추가된 선분을 나타낸다)

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15685/3.png

3세대 드래곤 커브도 2세대 드래곤 커브를 이용해 만들 수 있다. 아래 그림은 3세대 드래곤 커브이다.

!https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15685/4.png

즉, K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를?끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에?붙인 것이다.

크기가 100×100인 격자 위에 드래곤 커브가 N개 있다. 이때, 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하는 프로그램을 작성하시오. 격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표이다.

## 입력

첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 드래곤 커브의 정보가 주어진다. 드래곤 커브의 정보는 네?정수 x, y, d, g로 이루어져 있다. x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)

입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.

방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.

- 0: x좌표가 증가하는 방향 (→)
- 1: y좌표가 감소하는 방향 (↑)
- 2: x좌표가 감소하는 방향 (←)
- 3: y좌표가 증가하는 방향 (↓)

## 출력

첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.

## 예제 입력 1

```
3
3 3 0 1
4 2 1 3
4 2 2 1

```

## 예제 출력 1

```
4
```

### code

```python
import sys
input = sys.stdin.readline

n = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

# 좌표가 드래곤 커브에 포함이 되는지 체크해줄 리스트
check = [[0] * (101) for _ in range(101)]

for _  in range(n):
    x,y,d,g = map(int,input().split())

    # 주어진 g세대동안 움직인 방향들을 담아둘 리스트
    move_list = [d]
    # 먼저 시작하는 x,y 좌표는 방문체크
    check[x][y] = 1
    # 세대 만큼 For문을 돌리면서
    for i in range(g):
        tmp = []
        # 시작세대 d로 초기화한 move_list의 길이만 큼 for문을 돌린다.
        # 앞으로 계속 추가해줄 것이기 때문에 길이는 늘어난다.
        for j in range(len(move_list)):
            # 이전 세대들을 돌면서 뒤에서 부터  방향에 1씩 더하고 4로 나눠서 방향을 
            # tmp에 append 시킨다.
            tmp.append((move_list[-j-1]+1)%4)
        # move_list 에 tmp를 extend 시켜서 뒤에 그대로 붙여준다.
        move_list.extend(tmp)

    # g 세대 만큼 실행한 뒤 
    # move_list에 있는 방향들을 확인하면서 좌표를 계산해주고, check 처리를 해준다.
    for i in move_list:
        nx = x + dx[i]
        ny = y + dy[i]
        check[nx][ny] = 1 # 체크처리
        x,y = nx,ny # 방향을 현재 움직인 방향으로 갱신

answer = 0
# 100,100 좌표를 돌면서 한 좌표가 1로 체크되어있을 때, 
# 나머지 오른쪽, 아래, 오른쪽 아래대각선이 1로 체크되어있으면
# answer += 1  을 해준다.
for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i+1][j] == 1 and check[i][j+1] == 1 and check[i+1][j+1] == 1:
            answer += 1

print(answer)
```

### Solution

이 문제는 도저히 문제가 되지 않아서 못 풀었던 문제이다. 구현 자체에서 각 이동하는 방향을 규칙을 찾아서 리스트로 만들고 해당 좌표를 방문했을 시 따로 표기를 해둔다. 그리고 나중에 전체 좌표를 훑으면서 사각형의 개수를 세면 되는 문제인데, 입력 값이 무엇을 의미하는 지 문제를 제대로 이해하지 못했다. g값이 주어질 때 그 g값 만큼 드래곤 커브를 만들고 총 커브 개수를 종합적으로 세는 문제인지 추가적인 설명이 필요해 보였다,

## 2290 문제

지민이는 새로운 컴퓨터를 샀다. 하지만 새로운 컴퓨터에 사은품으로 온 LC-디스플레이 모니터가 잘 안나오는 것이다. 지민이의 친한 친구인 지환이는 지민이의 새로운 모니터를 위해 테스트 할 수 있는 프로그램을 만들기로 하였다.

## 입력

첫째 줄에 두 개의 정수 s와 n이 들어온다. (1 ≤ s ≤ 10, 0 ≤ n ≤ 9,999,999,999)이다. n은 LCD 모니터에 나타내야 할 수 이며, s는 크기이다.

## 출력

길이가 s인 '`-`'와 '`|`'를 이용해서 출력해야 한다. 각 숫자는 모두 s+2의 가로와 2s+3의 세로로 이루어 진다. 나머지는 공백으로 채워야 한다. 각 숫자의 사이에는 공백이 한 칸 있어야 한다.

## 예제 입력 1

```
2 1234567890

```

## 예제 출력 1

```
      --   --        --   --   --   --   --   --
   |    |    | |  | |    |       | |  | |  | |  |
   |    |    | |  | |    |       | |  | |  | |  |
      --   --   --   --   --        --   --
   | |       |    |    | |  |    | |  |    | |  |
   | |       |    |    | |  |    | |  |    | |  |
      --   --        --   --        --   --   --
```

### Code

```python
# s, n 입력 받기
s, n = input().split()
s = int(s)

# 숫자 표현을 리스트로 저장
number = [
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]      
]

# 7세그먼트 디스플레이의 각 라인에 대해서 반복
for lcd in range(7):
    # 3의 배수인 라인일 때 (숫자와 숫자 사이 출력)
    if lcd % 3 == 0:
        for num in n:
            idx = int(num)
            print(" ", end="")  # 공백 추가
            if number[idx][lcd]:
                for _ in range(s):
                    print("-", end="")  # "-" 출력
            else:
                for _ in range(s):
                    print(" ", end="")  # 공백 출력
            print("  ", end="")  # 숫자 사이 공백 출력
        print("")  # 줄바꿈
    # 1번 라인 또는 4번 라인일 때 (숫자 위 아래 출력)
    elif lcd == 1 or lcd == 4:
        for _ in range(s):
            for num in n:
                idx = int(num)
                if number[idx][lcd]:
                    print("|", end="")  # "|" 출력
                else:
                    print(" ", end="")  # 공백 출력
                for _ in range(s):
                    print(" ", end="")  # 공백 출력
                if number[idx][lcd + 1]:
                    print("|", end="")  # "|" 출력
                else:
                    print(" ", end="")  # 공백 출력
                print(" ", end="")  # 숫자 사이 공백 출력
            print("")  # 줄바꿈
```

### Solution

문제를 이해하는 데 오래 걸렸다.

먼저 LCD를 활용한 숫자 표기법을 알아야 한다. number 2차원 배열을 선언하고 0부터 9까지의 숫자에 해당하는 각각 불 켜지는 곳을 표시한다. 0은 안 켜지는 곳 1이 켜지는 곳이다.

양 옆 그리고 가운데를 제외한 s길이의 곳에 모두 글씨가 쓰여야 한다. LCD를 보니 0, 3, 6번째 전구에는 가로가 표시되고 나머지는 전부 세로로 표기가 된다. 따라서 3의 배수로 나누어 떨어지는 경우와 그렇지 않는 경우를 표기한다.

세로를 표시할 때는 줄 바꿈을 s만큼 해주어야 한다. 따라서 반복문을 돌리고 현재 열에 해당되는 n입력 값을 다시 탐색하고 숫자 비교를 해주어야만 한다.

<aside>
? 이 코드는 입력된 숫자를 7세그먼트 디스플레이 스타일로 표시하는 코드입니다. 디스플레이에는 각 숫자별로 7개의 선으로 이루어진 패턴이 있으며, 각 선이나 공백을 화면에 출력하고 필요한 공백을 추가하여 디스플레이를 생성합니다. 7세그먼트 디스플레이에서 각 숫자별로 어떤 선을 활성화해야 하는지를 **`number`** 리스트에 저장하고, 각 라인(0~6)에 대해 숫자와 숫자 사이, 숫자 위 아래에 어떤 패턴을 출력할지 결정합니다. 이를 통해 입력된 숫자를 7세그먼트 디스플레이 스타일로 표현할 수 있습니다.

</aside>

## 16931 문제

크기가 N×M인 종이가 있고, 종이는 1×1크기의 칸으로 나누어져 있다.?이 종이의 각 칸 위에?1×1×1 크기의 정육면체를 놓아 3차원 도형을 만들었다.

종이의 각 칸에 놓인 정육면체의 개수가 주어졌을 때, 이 도형의 겉넓이를 구하는 프로그램을 작성하시오.

https://upload.acmicpc.net/8d68cff7-fd62-4ae8-8b27-f8a5621e4ddd/-/preview/

위의 그림은 3×3 크기의 종이 위에 정육면체를 놓은 것이고, 겉넓이는 60이다.

## 입력

첫째 줄에 종이의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에는 종이의 각 칸에 놓인 정육면체의 수가 주어진다.

## 출력

첫째 줄에 도형의 겉넓이를 출력한다.

## 제한

- 1 ≤ N, M ≤ 100
- 1 ≤ 종이의 한 칸에 놓인 정육면체의 수 ≤ 100

## 예제 입력 1

```
1 1
1

```

## 예제 출력 1

```
6
```

### code

```python
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

up = N * M

left = 0
for i in range(N):
    for j in range(M):
        if j == 0:
            left += arr[i][j]
        else:
            if arr[i][j-1] < arr[i][j]:
                left += arr[i][j] - arr[i][j-1]

front = 0
for j in range(M):
    for i in range(N):
        if i == 0:
            front += arr[i][j]
        else:
            if arr[i-1][j] < arr[i][j]:
                front += arr[i][j] - arr[i-1][j]
        
answer = 2 * (up + left + front)
print(answer)
```

### Solution

1. 만약 현재 칸에 정육면체가 쌓여 있으면, 기본적으로 윗면과 아랫면의 겉넓이가 2로 더해집니다.
2. 현재 칸의 왼쪽 칸이 존재하면, 왼쪽 칸과의 높이 차이만큼의 겉넓이가 추가됩니다. 왼쪽 칸의 높이는 **`arr[i][j-1]`**이며, 현재 칸의 높이는 **`arr[i][j]`**입니다. 따라서 **`abs(arr[i][j] - arr[i][j - 1])`**을 더합니다. 단, 현재 칸이 가장 왼쪽 칸인 경우(즉, **`j`**가 0인 경우)에는 현재 칸의 높이가 추가됩니다.
3. 현재 칸의 오른쪽 칸이 존재하면, 오른쪽 칸과의 높이 차이만큼의 겉넓이가 추가됩니다. 오른쪽 칸의 높이는 **`arr[i][j+1]`**이며, 현재 칸의 높이는 **`arr[i][j]`**입니다. 따라서 **`abs(arr[i][j] - arr[i][j + 1])`**을 더합니다. 단, 현재 칸이 가장 오른쪽 칸인 경우(즉, **`j`**가 **`M - 1`**인 경우)에는 현재 칸의 높이가 추가됩니다.
4. 현재 칸의 윗 칸이 존재하면, 윗 칸과의 높이 차이만큼의 겉넓이가 추가됩니다. 윗 칸의 높이는 **`arr[i-1][j]`**이며, 현재 칸의 높이는 **`arr[i][j]`**입니다. 따라서 **`abs(arr[i][j] - arr[i-1][j])`**을 더합니다. 단, 현재 칸이 가장 윗 칸인 경우(즉, **`i`**가 0인 경우)에는 현재 칸의 높이가 추가됩니다.
5. 현재 칸의 아랫 칸이 존재하면, 아랫 칸과의 높이 차이만큼의 겉넓이가 추가됩니다. 아랫 칸의 높이는 **`arr[i+1][j]`**이며, 현재 칸의 높이는 **`arr[i][j]`**입니다. 따라서 **`abs(arr[i][j] - arr[i+1][j])`**을 더합니다. 단, 현재 칸이 가장 아랫 칸인 경우(즉, **`i`**가 **`N - 1`**인 경우)에는 현재 칸의 높이가 추가됩니다

## 1917 문제

여섯 개의 정사각형 모양의 종이가 있으면, 이를 적절히 이어 붙여서 정육면체의 전개도를 만들 수 있다. 정육면체의 전개도라는 것은, 선을 따라 종이를 적절히 접었을 때 정육면체를 완성할 수 있는 경우를 말한다.

예를 들면 아래의 모양은 정육면체의 전개도가 될 수 있다.

https://upload.acmicpc.net/8447549a-a7b4-45bb-ae14-7d9ea8348a7a/-/preview/

하지만 모든 경우에 정육면체를 만들 수 있는 것은 아니다. 예를 들어 다음과 같은 모양의 전개도는 여섯 개의 정사각형으로 이루어 있기는 하나 정육면체를 만들 수는 없다.

https://upload.acmicpc.net/a852ac4b-ccaa-4c16-8924-4c2a962d02c7/-/preview/

여섯 개의 정사각형으로 이루어진 전개도가 주어졌을 때, 이것이 정육면체의 전개도가 될 수 있는지 없는지를 가려내는 프로그램을 작성하시오.

## 입력

세 개의 입력 데이터가 주어지며, 각각의 입력 데이터는 여섯 개의 줄로 이루어져 있다. 각 데이터는 여섯 개의 줄에 걸쳐 여섯 개의 숫자가 빈 칸을 사이에 두고 주어진다. 숫자는 0 또는 1로 이루어지며, 36개의 숫자 중 1은 정확히 6개가 있다. 0은 공백을 나타내며 1은 정사각형을 나타낸다. (즉 전체의 그림이 전개도를 나타낸다고 보면 된다.) 정사각형들이 서로 떨어져 있는 경우는 없다.

## 출력

세 개의 줄에 걸쳐, 입력된 순서대로 전개도가 정육면체의 전개도이면 yes를, 아니면 no를 출력한다.

## 예제 입력 1

```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 0 0
0 1 1 1 1 0
0 0 1 0 0 0
0 0 0 0 0 0
0 1 1 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
1 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 1 1 0
0 0 1 1 0 0
0 0 0 1 1 0
0 0 0 0 0 0
0 0 0 0 0 0
```

## 예제 출력 1

```
yes
yes
no
```

### Code

```python
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dk = [1, 0, 3, 2]

def dice_move(k) :
  if k == 0 :
    dice_visited[0][1], dice_visited[1][1], dice_visited[2][1], dice_visited[3][1] = dice_visited[3][1], dice_visited[0][1], dice_visited[1][1], dice_visited[2][1]
  elif k == 1 :
    dice_visited[0][1], dice_visited[1][1], dice_visited[2][1], dice_visited[3][1] = dice_visited[1][1], dice_visited[2][1], dice_visited[3][1], dice_visited[0][1]
  elif k == 2 :
    dice_visited[1][0], dice_visited[1][1], dice_visited[1][2], dice_visited[3][1] = dice_visited[3][1], dice_visited[1][0], dice_visited[1][1], dice_visited[1][2]
  else :
    dice_visited[1][0], dice_visited[1][1], dice_visited[1][2], dice_visited[3][1] = dice_visited[1][1], dice_visited[1][2], dice_visited[3][1], dice_visited[1][0]

def dfs(x, y) :
  cnt = 1
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < 6 and -1 < ay < 6 and map_list[ay][ax] == 1 :
      dice_move(k)
      if not dice_visited[1][1] :
        dice_visited[1][1] = True
        cnt += dfs(ax, ay)
      dice_move(dk[k])
  return cnt

for _ in range(3) :
  map_list = [list(map(int, input().split())) for _ in range(6)]
  dice_visited = [[False]*3 for _ in range(4)]
  flg = False
  for i in range(6) :
    for j in range(6) :
      if map_list[i][j] == 1 :
        dice_visited[1][1] = True
        cnt = dfs(j, i)
        flg = True
        break
    if flg : 
      break
  print('yes' if cnt == 6 else 'no')
```

### Solution

**`dice_move(k)`** 함수는 **`k`** 값에 따라 주사각형을 회전시키는 함수로, **`k`**가 0일 경우 시계방향으로 회전하고, 1일 경우 반시계방향으로 회전하며, 2와 3일 경우 각각 180도와 반대 방향으로 90도 회전합니다.

**`dfs(x, y)`** 함수는 깊이 우선 탐색(DFS)을 사용하여 정육면체를 구성하는 주사각형들의 영역을 찾는 함수입니다. 시작 좌표 **`(x, y)`**에서 출발하여 주사각형을 이동하면서 영역을 찾고, 찾은 영역의 개수를 반환합니다.

마지막으로, 세 개의 테스트 케이스에 대해 각각 입력된 종이 모양(**`map_list`**)을 확인하며 주사각형이 있는 위치를 찾고, 해당 위치를 방문한 후 **`dfs`** 함수를 호출하여 정육면체의 영역을 찾습니다. 정육면체의 영역을 모두 찾으면 **`cnt`** 값이 6이 되며, 이 경우 "yes"를 출력하고 그렇지 않으면 "no"를 출력합니다.

## 16967 문제

크기가 H × W인 배열 A와 두 정수 X와 Y가 있을 때, 크기가 (H + X) × (W + Y)인 배열 B는 배열 A와?배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시킨 배열을?겹쳐 만들 수 있다. 수가 겹쳐지면 수가 합쳐진다.

즉, 배열 B의 (i, j)에 들어있는 값은 아래 3개 중 하나이다.

- (i, j)가 두 배열 모두에 포함되지 않으면, B?= 0이다.
    
    i,j
    
- (i, j)가 두 배열 모두에 포함되면, B?= A?+ A이다.
    
    i,j
    
    i,j
    
    i-X,j-Y
    
- (i, j)가 두 배열 중 하나에 포함되면, B?= A?또는 A이다.
    
    i,j
    
    i,j
    
    i-X,j-Y
    

배열 B와 정수 X, Y가 주어졌을 때, 배열 A를 구해보자.

## 입력

첫째 줄에 네 정수 H, W, X, Y가 주어진다. 둘째 줄부터 H + X개의 줄에 배열 B의 원소가 주어진다.

항상 배열 A가 존재하는 경우만 입력으로 주어진다.

## 출력

총 H개의 줄에 배열 A의 원소를 출력한다.

## 제한

- 2 ≤ H, W ≤ 300
- 1 ≤ X < H
- 1 ≤ Y < W
- 0 ≤ B?≤ 1,000
    
    i,j
    

## 예제 입력 1

```
2 4 1 1
1 2 3 4 0
5 7 9 11 4
0 5 6 7 8

```

## 예제 출력 1

```
1 2 3 4
5 6 7 8
```

### Code

```python
h, w, x, y = map(int, input().split())

ans = []
graph = []

for _ in range(h+x):
    graph.append(list(map(int, input().split())))

for i in range(h):
    ans.append(graph[i][:w])

for i in range(h):
    for j in range(w):
        if i+x < h and j+y < w:
            ans[i+x][j+y] -= ans[i][j]

for a in ans:
    print(" ".join(map(str,a)))
```
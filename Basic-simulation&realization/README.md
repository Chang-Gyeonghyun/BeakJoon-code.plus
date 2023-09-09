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
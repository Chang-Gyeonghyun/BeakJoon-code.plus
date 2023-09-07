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
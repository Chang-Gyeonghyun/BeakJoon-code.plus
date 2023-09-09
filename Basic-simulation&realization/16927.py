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
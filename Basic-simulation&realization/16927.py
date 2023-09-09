N, M, R = map(int, input().split())  # N, M, R ���� �Է¹޽��ϴ�.
arr = [list(map(int, input().split())) for _ in range(N)]  # N���� �ٿ� �迭 A�� ���Ҹ� �Է¹޾� 2���� ����Ʈ�� �����մϴ�.

def rotate_array(N, M, arr):
    # ȸ�� ������ ������ Ƚ���� �ּҷ� ���̱� ���� �迭�� �׷����� �����ϴ�.
    num_layers = min(N, M) // 2
    rotated_arr = [row[:] for row in arr]  # �Է� �迭�� ������ �迭�� ����ϴ�.

    for layer in range(num_layers):
        # ���� �׷쿡���� ȸ�� ���� Ƚ���� ����մϴ�.
        num_rotations = R % (2 * (N + M - 4 * layer - 2))

        for _ in range(num_rotations):
            # ���� �׷쿡�� �� ���� ȸ���� �����մϴ�.
            temp = rotated_arr[layer][layer]  # ���� �׷��� ���� �� ���Ҹ� �ӽ÷� �����մϴ�.

            # ���� �� ȸ��: ���� ���� ���ҵ��� �� ĭ�� ���������� �̵���ŵ�ϴ�.
            for i in range(layer, M - layer - 1):
                rotated_arr[layer][i] = rotated_arr[layer][i + 1]

            # �Ʒ��� �� ȸ��: �Ʒ��� ���� ���ҵ��� �� ĭ�� ���� �̵���ŵ�ϴ�.
            for i in range(layer, N - layer - 1):
                rotated_arr[i][M - layer - 1] = rotated_arr[i + 1][M - layer - 1]

            # ������ �� ȸ��: ������ ���� ���ҵ��� �� ĭ�� �������� �̵���ŵ�ϴ�.
            for i in range(M - layer - 1, layer, -1):
                rotated_arr[N - layer - 1][i] = rotated_arr[N - layer - 1][i - 1]

            # ���� �� ȸ��: ���� ���� ���ҵ��� �� ĭ�� �Ʒ��� �̵���ŵ�ϴ�.
            for i in range(N - layer - 1, layer + 1, -1):
                rotated_arr[i][layer] = rotated_arr[i - 1][layer]

            # ȸ���� ��ġ�� �ӽ÷� ������ ���� ������ �Ʒ� ���ҿ� �����մϴ�.
            rotated_arr[layer + 1][layer] = temp

    return rotated_arr  # ȸ���� �迭�� ��ȯ�մϴ�.

result = rotate_array(N, M, arr)  # rotate_array �Լ��� ȣ���Ͽ� �迭�� ȸ����ŵ�ϴ�.

for row in result:  # ȸ���� ��ģ �迭�� ����մϴ�.
    print(" ".join(map(str, row)))  # ������ �̿��Ͽ� �� �ٿ� ����մϴ�.
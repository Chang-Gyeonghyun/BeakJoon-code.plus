def bitmask():
    global maxAns
    # ��Ʈ����ũ�� 2^(N*M)�� ����� ���� ��������
    for i in range(1 << n * m):
        total = 0
        # ���� �� ���
        for row in range(n):
            rowsum = 0
            for col in range(m):
                # idx �� ������ �迭�� �Ϸķ� �÷������� �ε����� ������� �ǹ�
                idx = row * m + col
                # �����϶�
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + arr[row][col]
                # �����϶� �տ��� ���� ���� total�� ���ϰ� rowsum �ʱ�ȭ
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        # ���� �� ���
        for col in range(m):
            colsum = 0
            for row in range(n):
                # idx �� ������ �迭�� �Ϸķ� �÷������� �ε����� ������� �ǹ�
                idx = row * m + col
                # �����϶�
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + arr[row][col]
                # �����϶� �տ��� ���� ���� total�� ���ϰ� colsum �ʱ�ȭ
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        maxAns = max(maxAns, total)


n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

maxAns = 0
bitmask()
print(maxAns)

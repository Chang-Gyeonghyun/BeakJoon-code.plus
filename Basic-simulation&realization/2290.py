# s, n �Է� �ޱ�
s, n = input().split()
s = int(s)

# ���� ǥ���� ����Ʈ�� ����
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

# 7���׸�Ʈ ���÷����� �� ���ο� ���ؼ� �ݺ�
for lcd in range(7):
    # 3�� ����� ������ �� (���ڿ� ���� ���� ���)
    if lcd % 3 == 0:
        for num in n:
            idx = int(num)
            print(" ", end="")  # ���� �߰�
            if number[idx][lcd]:
                for _ in range(s):
                    print("-", end="")  # "-" ���
            else:
                for _ in range(s):
                    print(" ", end="")  # ���� ���
            print("  ", end="")  # ���� ���� ���� ���
        print("")  # �ٹٲ�
    # 1�� ���� �Ǵ� 4�� ������ �� (���� �� �Ʒ� ���)
    elif lcd == 1 or lcd == 4:
        for _ in range(s):
            for num in n:
                idx = int(num)
                if number[idx][lcd]:
                    print("|", end="")  # "|" ���
                else:
                    print(" ", end="")  # ���� ���
                for _ in range(s):
                    print(" ", end="")  # ���� ���
                if number[idx][lcd + 1]:
                    print("|", end="")  # "|" ���
                else:
                    print(" ", end="")  # ���� ���
                print(" ", end="")  # ���� ���� ���� ���
            print("")  # �ٹٲ�

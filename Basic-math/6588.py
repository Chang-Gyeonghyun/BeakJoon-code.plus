n = 1000001
# �Ҽ� �ƴ� ��� Ȧ�� ó��
table = [1] * n
for i in range(3, int(n ** 0.5) + 1, 2):
    if table[i]:
        for j in range(i * 2, n, i):
            table[j] = 0
# k�� ��������� �� Ȧ���� �Ҽ� �˻�
while 1:
    k = int(input())
    if not k:
        break
    for i in range(3, int(k / 2) + 1, 2):
        if table[i] and table[k - i]:
            print(f"{k} = {i} + {k - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
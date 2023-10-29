T = int(input())
arr = [list(map(int, input())) for _ in range(T)]
K = int(input())
rotation = []

def rotate(index, direction):
    if index < 0 or index >= T:
        return  # �ε����� ������ ����� ����
    
    visited[index] = True  # �湮�� ��Ϲ��� ���

    # ���� ��Ϲ����� Ȯ���ϰ� ȸ��
    if index > 0 and arr[index][6] != arr[index - 1][2] and not visited[index - 1]:
        rotate(index - 1, -direction)
    # ������ ��Ϲ����� Ȯ���ϰ� ȸ��
    if index < T - 1 and arr[index][2] != arr[index + 1][6] and not visited[index + 1]:
        rotate(index + 1, -direction)
    
    # ���� ��Ϲ��� ȸ��
    if direction == 1:
        arr[index].insert(0, arr[index].pop())
    else:
        arr[index].append(arr[index].pop(0))


for _ in range(K):
    index, direction = map(int, input().split())
    rotation.append((index - 1, direction))  # �ε����� 0���� �����ϵ��� ����

for index, direction in rotation:
    visited = [False] * T  # �� ȸ������ �湮 ���� �ʱ�ȭ
    rotate(index, direction)
    
count_s = 0
for i in range(T):
    if arr[i][0] == 1:
        count_s += 1
        
print(count_s)

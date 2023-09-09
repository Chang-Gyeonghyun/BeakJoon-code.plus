n, l = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0

def pos(now) :
    for j in range(1, n) :
        if abs(now[j] - now[j-1]) > 1 : # ���̰� 1�� ������ False ��ȯ
            return False
        if now[j] < now[j-1] : # ���� < ���� �̸� ���θ� ����� ���� �������� ��ĵ(���� ���� ��ġ)
            for k in range(l) :
                if j+k >= n or used[j+k] or now[j] != now[j+k] : # ������ �Ѿ�ų� �̹� ��ġ�Ǿ� �ְų� ���̰� �ٸ� ��� False ��ȯ
                    return False
                if now[j] == now[j+k] : # ���̰� ���� ��� �湮 ó��
                    used[j+k] = True
        elif now[j] > now[j-1] : # ���� > ���� �̸� ���θ� ����� ���� ������ ��ĵ(���� ���� ��ġ)
            for k in range(l) :
                if j-k-1 < 0 or now[j-1] != now[j-k-1] or used[j-k-1] : # ������ �Ѿ�ų� �̹� ��ġ�Ǿ� �ְų� ���̰� �ٸ� ��� False ��ȯ
                    return False
                if now[j-1] == now[j-k-1] : # ���̰� ���� ��� �湮 ó��
                    used[j-k-1] = True
    return True

# ���� Ȯ��
for i in range(n) :
    used = [False for _ in range(n)] # �湮 ó��
    if pos(data[i]) :
        result += 1

# ���� Ȯ��
for i in range(n) :
    used = [False for _ in range(n)] # �湮 ó��
    if pos([data[j][i] for j in range(n)]) :
        result += 1

print(result)
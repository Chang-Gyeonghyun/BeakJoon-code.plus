# def yaksu(a):
#     sum = 0
#     f = set()
#     for i in range(a):
#         if a%(i+1) == 0:
#             f.add(i+1)
#     while len(f) >= 1:
#         sum += f.pop()
#     return sum
        
# N = int(input())
# sum = 0
# for i in range(N):
#     sum += yaksu(i+1)
# print(sum)

# ���� ��� �ð� ���⵵�� n^2�� �ð� �ʰ��� �ȴ�. ���� �Ʒ� ���� �ڵ�� �ٲ��ش�.

n = int(input())

sum_ = 0
for i in range(1, n+1):
	# i�� ����� ���� = i�� ����� ���� ��
    sum_ += (n//i)*i

print(sum_)
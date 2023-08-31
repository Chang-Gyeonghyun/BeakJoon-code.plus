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

# 위의 경우 시간 복잡도가 n^2라서 시간 초과가 된다. 따라서 아래 정답 코드로 바꿔준다.

n = int(input())

sum_ = 0
for i in range(1, n+1):
	# i의 배수의 개수 = i를 약수로 갖는 수
    sum_ += (n//i)*i

print(sum_)
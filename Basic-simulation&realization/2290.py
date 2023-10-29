# s, n 입력 받기
s, n = input().split()
s = int(s)

# 숫자 표현을 리스트로 저장
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

# 7세그먼트 디스플레이의 각 라인에 대해서 반복
for lcd in range(7):
    # 3의 배수인 라인일 때 (숫자와 숫자 사이 출력)
    if lcd % 3 == 0:
        for num in n:
            idx = int(num)
            print(" ", end="")  # 공백 추가
            if number[idx][lcd]:
                for _ in range(s):
                    print("-", end="")  # "-" 출력
            else:
                for _ in range(s):
                    print(" ", end="")  # 공백 출력
            print("  ", end="")  # 숫자 사이 공백 출력
        print("")  # 줄바꿈
    # 1번 라인 또는 4번 라인일 때 (숫자 위 아래 출력)
    elif lcd == 1 or lcd == 4:
        for _ in range(s):
            for num in n:
                idx = int(num)
                if number[idx][lcd]:
                    print("|", end="")  # "|" 출력
                else:
                    print(" ", end="")  # 공백 출력
                for _ in range(s):
                    print(" ", end="")  # 공백 출력
                if number[idx][lcd + 1]:
                    print("|", end="")  # "|" 출력
                else:
                    print(" ", end="")  # 공백 출력
                print(" ", end="")  # 숫자 사이 공백 출력
            print("")  # 줄바꿈

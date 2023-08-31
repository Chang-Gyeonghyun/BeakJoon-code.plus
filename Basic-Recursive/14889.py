import sys

N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]


start = []
link = []
result = sys.maxsize

def dfs(head):
    global link, result
    if len(start) == N/2:
        link = [ele for ele in range(N) if ele not in start] #나머지 인원들은 link팀에 배치
        differ = find(start) - find(link)
        result = min(result,abs(differ))
        return
        
    
    
    for i in range(head, N): #팀원 뽑기
        start.append(i)
        dfs(i+1) #중복됨으로 인덱스를 굳이 처음부터 셀 필요 없다.
        start.pop()
        
        
def find(arr:list):  #s리스트 안에서 팀원간 능력치 찾고 더하기
    sum = 0
    for i in arr:
        for j in arr:
            sum += s[i][j]
    return sum
        
dfs(0)
print(result)
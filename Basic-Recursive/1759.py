L, C = map(int,input().split())
arr = list(input().split())
arr.sort()

stack = []
mom = ['a', 'e', 'i', 'o', 'u'] #���� ����Ʈ

def dfs():
    if len(stack) == L:
        momv = False
        sonv = 0
        
        for i in stack: #���� ���� ���� ����
            if i in mom:
                momv = True
            else:
                sonv += 1

        if momv and sonv>=2:
            print("".join(stack))
        return
            
    
    for i in arr:
        if not stack or i > stack[-1]:
            stack.append(i)
            dfs()
            stack.pop()
            
            
dfs()
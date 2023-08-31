def dfs(stack):
    if len(stack) == 6:
        print(" ".join(map(str,stack)))
        return
    for i in s:
        if not stack or i > stack[-1]:
            stack.append(i)
            dfs(stack)
            stack.pop()

while True:
    s = list(map(int,input().split()))
    k = s[0]
    s = s[1:]
    if k == 0:
        exit()
    stack = []
    dfs(stack)
    print()
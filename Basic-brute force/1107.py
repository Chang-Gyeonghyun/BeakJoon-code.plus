def find(N):
    for i in fault_num:
        if str(N).find(i) >= 0:
            return True
    return False

cur_ch = 100
prefer_ch = int(input())
N = int(input())
if N != 0:
    fault_num = list(input().split())
else:
    fault_num = []

#나중에 자릿수를 센다. 그주변에서 위 아래로 다 가보고 가장 최소
count, finalnum = 0,0

UN = prefer_ch
DN = prefer_ch
temp = abs(cur_ch - prefer_ch)
valid = True

if prefer_ch == 100:
    print("0")

elif N == 10:
    print(temp)
    
else:
    while True:
        
        if find(DN) and valid:
            DN -= 1
            if(DN < 0):
                valid = False
        else:
            if valid:
                count = prefer_ch - DN
                finalnum = DN
                break
        if find(UN):
            UN += 1
        else:
            count = UN - prefer_ch
            finalnum = UN
            break
    #print(finalnum ,len(str(finalnum)) , count)
    print(min(len(str(finalnum)) + count, temp))
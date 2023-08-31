while True:
    try:
         i = int(input())
    except:
        break
    count = '1'
    countnum = 1
    while True:
        if (int(count))%i == 0:
            break
        else:
            count += '1'
            countnum += 1
    print(countnum)
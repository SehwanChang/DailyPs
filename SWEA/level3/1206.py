for i in range(1, 11) :
    cnt = 0
    n = int(input())
    buildings = list(map(int,input().split()))
    checked = [0, 1, len(buildings) - 1, len(buildings) - 2]
    tmp = []
    for idx, height in enumerate(buildings) :
        if idx in checked :
            continue
        target = max(max(buildings[idx - 2: idx]), max(buildings[idx + 1: idx + 3]))
        if height > target:
            cnt += height - target
        tmp.append(cnt)
    print(*tmp)
    print("#{} {}".format(i, cnt))  
#8  
#0 0 3 5 2 4 9 0 6 4 0 6 0 0
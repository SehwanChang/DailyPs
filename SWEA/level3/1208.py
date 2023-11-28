for i in range(1, 11) :
    dump = int(input())
    height = list(map(int, input().split()))
    
    for j in range(dump) :
        height.sort()
        height[0] += 1
        height[-1] -= 1
    ans = max(height) - min(height)
    print("#{} {}".format(i, ans))
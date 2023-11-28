for test in range(1, 11) :
    num = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    end = 0 
    for i in range(100) :
        if ladder[99][i] == 2 :
            end = i
    current = end
    for j in range(99, 0, -1) :
        if current > 0 and ladder[j][current - 1] :
            while current > 0 and ladder[j][current - 1] :
                current -= 1
        elif current < 99 and ladder[j][current + 1] :
             while current < 99 and ladder[j][current + 1] :
                current += 1

    print("#{} {}".format(test, current))
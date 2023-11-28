for tc in range(1, 11) :
    n = int(input())
    cnt = 0
    palindrome = [list(input()) for i in range(8)]
    for i in range(8) :
        for j in range(8) :
            # 가로
            if j + n <= 8 :
                tmp = palindrome[i][j : j + n]
                if tmp == tmp[::-1] : 
                    cnt += 1
            # 세로
            if i + n <= 8 :
                tmp = [palindrome[k][j] for k in range(i, i + n)]
                if tmp == tmp[::-1] : 
                    cnt += 1

    print("#{} {}".format(tc, cnt))

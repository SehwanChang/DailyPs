def check(i, j, board) :
    c = board[i][j]
    if c == '.' :
        return False
    if c == board[i][j + 1] and c == board[i + 1][j] and c == board[i + 1][j + 1] :
        return True
    else :
        return False


def solution(m, n, board):
    answer = 0
    for i in range(m) :
        board[i] = list(board[i])
        
    while True :
        #터트려야 할 위치 체크 
        checked = [[0] * n for _ in range(m)]
        for i in range(m -1) :
            for j in range(n - 1) :
                #같은 캐릭터가 있는 위치 체크 
                if check(i, j, board) :
                    checked[i][j] = 1
                    checked[i + 1][j] = 1
                    checked[i][j + 1] = 1
                    checked[i + 1][j + 1] = 1
                
        
        #터트려야할 문자가 있는지 체크 , 없으면 리턴
        cnt = 0
        for data in checked :
            cnt += data.count(1)
        
        if cnt == 0 :
            break
        answer += cnt 
        
        for j in range(n) :
            for i in range(m) :
                if checked[i][j] == 1 :
                    x, y = i, j
                    while x >= 0 :
                        if x == 0 :
                            board[x][y] = '.'
                            break
                        else :
                            board[x][y] = board[x - 1][y]
                        x -= 1
    return answer
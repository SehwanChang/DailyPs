import sys
input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]


def row(x, num) :
    for i in range(9) :
        if num == sudoku[x][i] :
            return False
    return True

def col(y, num) :
    for i in range(9) :
        if num == sudoku[i][y] :
            return False
    return True

def box(x, y, num) :
    nx = x // 3 * 3 
    ny = y // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if num == sudoku[nx + i][ny + j] :
                return False
    return True

blank = []

def back_tracking(level) :
    if level == len(blank) :
        for rows in sudoku :
            print(*rows)
        sys.exit()

    for i in range(1, 10) :
        x, y = blank[level]
        if row(x, i) and col(y, i) and box(x, y, i) :
            sudoku[x][y] = i
            back_tracking(level + 1)
            sudoku[x][y] = 0

for i in range(9) :
    for j in range(9) : 
        if sudoku[i][j] == 0 :
            blank.append((i, j))
back_tracking(0)  


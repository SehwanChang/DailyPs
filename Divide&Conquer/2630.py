import sys
input = sys.stdin.readline
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def divide(x, y, n) :
    global white, blue
    color = graph[x][y]
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if color != graph[i][j] :
                divide(x, y, n // 2)
                divide(x, y + n //2, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x + n // 2 , y + n // 2, n // 2)
                return
    if color == 0 :
        white += 1
    else :
        blue += 1
divide(0, 0, n)
print(white)
print(blue)
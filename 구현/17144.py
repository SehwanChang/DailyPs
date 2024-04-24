import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x1, x2 = 0, 0
for i in range(r) :
    if graph[i][0] == -1 :
        x1 , x2 = i, i + 1
        break
def spread(graph) :
    new_graph = [[0] * c for _ in range(r)]
    for x in range(r) :
        for y in range(c) :
            if graph[x][y] > 0:
                amount = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1 :
                        new_graph[nx][ny] += graph[x][y] // 5
                        amount += graph[x][y] // 5
                new_graph[x][y] += graph[x][y] - amount
            if graph[x][y] == -1 :
                new_graph[x][y] = -1
    return new_graph

def after_purify(dust) : 
    #청정기 상단부
    for i in range(x1 - 1, -1, -1) :
        if i + 1 == x1 :
            dust[i][0] = 0
            continue
        dust[i + 1][0] = dust[i][0]
    dust[0][0] = 0

    for i in range(1, c) :
        dust[0][i - 1] = dust[0][i]
    dust[0][c - 1] = 0    

    for i in range(1, x1 + 1) :
        dust[i - 1][c - 1] = dust[i][c - 1]
    dust[x1][c - 1] = 0   
        
    for i in range(c - 2, 0, -1) :
        dust[x1][i + 1] = dust[x1][i]
    dust[x1][1] = 0
    #청정기 하단부
    for i in range(x2 + 1, r) :
        if dust[i - 1][0] == -1 :
            dust[i][0] = 0
            continue
        dust[i - 1][0] = dust[i][0] 
    dust[r - 1][0] = 0

    for i in range(1, c) :
        dust[r - 1][i - 1] = dust[r - 1][i]
    dust[r - 1][c - 1] = 0
    for i in range(r - 2, x2 - 1, -1) :
        dust[i + 1][c - 1] = dust[i][c - 1]
    dust[x2][c - 1] = 0
    for i in range(c - 2, 0, -1) :
        dust[x2][i + 1] = dust[x2][i]
    dust[x2][1] = 0
    return dust

for i in range(t) :
    graph = spread(graph)
    graph = after_purify(graph)

ans = 0
for x in range(r) :
    for y in range(c) :
        if graph[x][y] != -1 :
            ans += graph[x][y]
print(ans)
# print('여기야')
# for i in range(r) :
#     print(*dust_graph[i])


#미세먼지 확산 : 모든칸에서 동시. 확산되는 양 : 1/5
#남은 먼지의 양 : 기존 -[기존 / 5] * 확산방향 개수
#공기청정기 :위 -> 반시계, 아래 -> 시계
#미세먼지가 공기청정기로 들어가면 모두 정화
#t초후 미세먼지의 양 

# 7 8 1
# 0 0 0 0 0 0 1 8
# 0 0 1 0 3 0 5 6
# -1 2 1 1 0 4 6 5
# -1 5 2 0 0 2 12 0
# 0 1 1 0 5 10 13 8
# 0 1 9 4 3 5 12 0
# 0 8 17 8 3 4 8 4

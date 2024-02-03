import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

#외부 공기와 내부 공기  구분하는것 필요
def dfs(x, y) :
    if 0 <= x < n and 0 <= y < m :
        if visited[x][y] or graph[x][y] == 1 :
            return
        visited[x][y] = True
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

for i in range(n) :
    dfs(i, 0)
    dfs(i, m - 1)
for j in range(m) :
    dfs(0, j)
    dfs(n - 1, j)


#녹는 조건 확인 , 외부 공기와 접촉하는 면수 세서 녹일 치즈목록에 추가 
#치즈 녹이기 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def melt_cheese() :
    meleting_cheese = []
    for x in range(n) :
        for y in range(m) :
            if graph[x][y] == 1 :
                air_contact = 0
                for i in range(4) :
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] :
                        air_contact += 1
                if air_contact >= 2 :
                    meleting_cheese.append((x, y))
    return meleting_cheese

def update_air() :
    for i in range(n) :
        visited[i] = [False] * m
    dfs(0, 0)
#외부공기 다시 갱신 
#반복 
time = 0
while True :
    melt_list = melt_cheese()
    if not melt_list :
        break
    for x, y in melt_list :
        graph[x][y] = 0
    update_air()
    time += 1
print(time)
import sys
input = sys.stdin.readline
n, m , x, y, k  = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
graph[x][y] = 0
direction = [[], [0, 1], [0, -1], [-1, 0], [1, 0]] # 동 서 북 남
dice = [0, 0, 0, 0, 0, 0] #탑, 바텀, 동, 서, 남, 북

def roll_dice(dice, order) :
    top, bottom, north, east, south, west = dice
    if order == 1: #동쪽 . 북, 남 뺴고는 다 바뀜 : 동 = 탑, 탑 = 서, 서 = 바텀, 바텀 = 동 
        new_east = top
        new_top = west
        new_west = bottom
        new_bottom = east
        new_north, new_south = north, south

    
    elif order == 2: #서쪽. 북, 남 뺴고는 다바뀜 : 탑 = 동, 동 = 바텀, 바텀 = 서, 서 = 탑
        new_top = east
        new_east = bottom
        new_bottom = west
        new_west = top
        new_north, new_south = north, south
    
    elif order == 3: #북쪽 .동, 서 빼고는 다 바뀜 탑 = 남, 남 = 바텀, 바텀 = 북, 북 = 탑
        new_top = south
        new_south = bottom
        new_bottom = north
        new_north = top
        new_east, new_west = east, west

    elif order == 4 :#남쪽 . 동, 서 빼고는 다 바뀜  탑 = 북, 북 = 바텀, 바텀 = 남, 남 = 탑
        new_top = north
        new_north = bottom
        new_bottom = south
        new_south = top
        new_east, new_west = east, west
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = new_top, new_bottom, new_north, new_east, new_south, new_west

for order in orders : 
    nx = x + direction[order][0]
    ny = y + direction[order][1]

    if 0 <= nx < n and 0 <= ny < m :
        roll_dice(dice, order)
        if graph[nx][ny] == 0 :
            graph[nx][ny] = dice[1]
        else :
            dice[1] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])

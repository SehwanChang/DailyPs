from collections import deque
n = int(input())
dummy = [[0] * (n) for _ in range(n)]
apple = []

snake = deque([(0, 0)])

move = []
k = int(input())
for j in range(k) :
    r, c = map(int, input().split())
    dummy[r - 1][c - 1] = 1
l = int(input())
for _ in range(l) :
    x, c = input().split()
    x = int(x)
    move.append((x,c))

#상 우 하 좌
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir_idx = 1

def turn(direction) :
    global dir_idx
    if direction == 'L' :
        dir_idx = (dir_idx - 1) % 4
    elif direction == 'D' :
        dir_idx = (dir_idx + 1) % 4

next_turn, turn_dir = move.pop(0)
time = 0
while True :
    time += 1
    head_x, head_y = snake[0]
    nx, ny = head_x + directions[dir_idx][0], head_y + directions[dir_idx][1]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake :
        break
    if dummy[nx][ny] == 1:
            dummy[nx][ny] = 0
            snake.appendleft((nx, ny))  
    else : 
        snake.appendleft((nx, ny))
        snake.pop()
    if time == next_turn:
        turn(turn_dir)
        if move:
            next_turn, turn_dir = move.pop(0)
    
print(time)
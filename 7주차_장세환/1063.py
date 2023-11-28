king , rock , n = input().split()
n = int(n)
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(rock[0]) - 64, rock[1]]))
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
for i in range(n) :
    m = input()

    dx = k[0] + move[m][0]
    dy = k[1] + move[m][1]
    
    if 0 < dx <= 8 and 0 < dy <= 8 :
        if dx == s[0]  and dy == s[1] :
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [dx, dy] 
                s = [sx, sy] 
        else :
            k = [dx, dy]
print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')
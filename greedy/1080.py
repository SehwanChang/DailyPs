n, m = map(int, input().split())

list_a = []
for i in range(n) :
    list_a.append(list(map(int,input())))

list_b = []
for i in range(n) :
    list_b.append(list(map(int,input())))

def check(i, j) :
    for x in range(i, i + 3) :
        for y in range(j, j + 3) :
            if list_a[x][y] == 1 : 
                list_a[x][y] = 0
            else : 
                list_a[x][y] = 1
cnt = 0 
if n < 3 and m < 3 and list_a != list_b :
    cnt = -1
else : 
    for row in range(n - 2) :
        for col in range(m - 2) :
            if list_a[row][col] != list_b[row][col] :
                cnt += 1
                check(row, col)
if list_a != list_b : 
        cnt = -1
print(cnt)
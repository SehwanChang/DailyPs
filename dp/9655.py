n = int(input())
win = [-1]*10001
win[1] = 1 
win[2] = 0 
win[3] = 1 

for i in range(4,n+1):
    if win[i-1] == 1 or win[i-3] == 1:
        win[i] = 0
    else:
        win[i] = 1

if win[n]==1:
    print('SK')
else:
    print('CY')
t = int(input())
for i in range(1, t + 1) :
    n = int(input())
    cnt = 0
    hays = [int(input()) for j in range(n)]
    average_hey = sum(hays) // n 
    scarce_hey = []
    cnt = sum([hay - average_hey for hay in hays if hay > average_hey])
    print("#{} {}".format(i, cnt))
#10 7 2 1 : 7번 필요 (전부 5)
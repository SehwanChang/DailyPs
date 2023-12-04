import sys
input = sys.stdin.readline
n, m = map(int,input().split())
price_list = []
for i in range(m) :
    price_list.append(list(map(int,input().split()))) 
price_list.sort(key= lambda x : (x[0], x[1]))


min_bundle = price_list[0][0]
min_each = min(price[1] for price in price_list)
cost = 0

while n > 0 :
    if n < 6 : 
        cost += min(min_bundle, n * min_each) 
        break
    cost += min(min_bundle, 6 * min_each)
    n -= 6
print(cost)




# 10 3
# 20 8
# 40 7
# 60 4
# 6개 -> 20원 
# 1개 -> 4원 4 x 4 = 16원 
# 토탈 = 36원

# 17 1
# 12 3
#18개 ->12 * 3 = 36원
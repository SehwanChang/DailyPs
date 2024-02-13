import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
entrance_dict = defaultdict()
for i in range(n) :
    word = input().rstrip()
    entrance_dict[word] = (i + 1)
exit = [input().strip() for _ in range(n)]
orders = []
for i in range(n) :
    orders.append(entrance_dict[exit[i]])

cnt = 0
for i in range(len(orders)) :
    for j in range(i, len(orders)):
        if orders[i] > orders[j] :
            cnt += 1
            break
print(cnt)


# 4 : 1대
# ZG431SN 1
# ZG5080K 2 
# ST123D 3
# ZG206A 4

# ZG206A  : 얘가 추월함  4
# ZG431SN  1
# ZG5080K 2
# ST123D 3

# 5 : 3대
# ZG508OK 1
# PU305A 2
# RI604B 3
# ZG206A 4
# ZG232ZF 5

# PU305A : 얘가 추월함. 3 
# ZG232ZF : 얘가 추월함.5
# ZG206A : 얘가 추월함. 4
# ZG508OK 1
# RI604B 2


# 5 : 2대
# ZG206A  1
# PU234Q  2
# OS945CK 3
# ZG431SN 4
# ZG5962J 5

# ZG5962J : 얘가 추월함. 5
# OS945CK : 얘가 추월함. 3
# ZG206A  1
# PU234Q 2
# ZG431SN 4
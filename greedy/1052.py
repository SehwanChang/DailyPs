n, k = map(int, input().split())
cnt = 0 
while bin(n).count('1') > k :
    n += 1
    cnt += 1
print(cnt)

# 사야하는 물병의 최솟값, 정답 x : -1
# 물병의 사이즈 = 무한대
# 비어있지 않은 물병 최대 갯수 = k개 
# 같은 양의 물이 들어있어야만 옮길 수 있음 
# 처음 :모든 물병이 1L
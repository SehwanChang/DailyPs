import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(str, input().split()))
expanded = []
for idx, num in enumerate(nums) :
    tmp_num = num * 9
    expanded.append((tmp_num, idx))
expanded.sort(key=lambda x : x[0], reverse=True)
ans = ''
for num, idx in expanded :
    ans += nums[idx]
if int(ans) == 0 :
    print(0)
else : 
    print(ans)
#0으로 시작 x, 0이 정답 : 0 출력 
#포함된 수 나열해서 가장 큰 수 만들기 

#우선순위 : 첫자리 숫자가 큰것, 첫자리 숫자가 같음 -> 두번쨰 숫자 or 자릿수 적은것
#비교할떄 같은 자릿수로 만들기 ex) 3과 321 : 333, 321
#최대 9자리니까 9자리로 변경하기 

#반례 
# 1) 자릿수 같은경우 
# 4 
# 3 2 3 3

# 2) 자릿수 다 다름, 앞자리수 다 같음
# 3
# 1 12 129

# 3) 모두 0

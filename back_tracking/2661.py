import sys
input = sys.stdin.readline
n = int(input())
nums = ['1', '2', '3']

def check(num) :
    for i in range(1, len(num) // 2 + 1) :
        #최근 추가된 원소들이 부분문자열을 포함하는지 체크 : 핵심
        if num[-i: ] == num[-(i * 2) : -i] :
            return False
        # 123 321 , i = 3 : 321, 123
        # 12332123 , i = 4 : 2123 1233
    else :
        return True 

def back_tracking(num) :
    if len(num) == n :
        print(num)
        sys.exit()
    for i in nums : 
        if check(num + i) :
            back_tracking(num + i)
    
back_tracking('1')

# num[-i: ] num 의 끝부터 i개 문자 포함하는 부분문자열 반환 
# num[-(i * 2) : -i]
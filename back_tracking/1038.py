import sys
input = sys.stdin.readline
nums = [str(i) for i in range(10)]
n = int(input().strip())
if n > 1022 : 
    print(-1)
    sys.exit()
cnt = 1  #자릿수

while cnt < 10 :
    for i in nums :
        if len(i) == cnt : 
            for j in range(10) :
                if int(i[-1]) > j :
                    nums.append(i + str(j))
    cnt += 1

print(nums[n])
T = int(input())

for test_case in range(1, T + 1):
    case_num = int(input())
    score_list = map(int,input().split())
    score_dict = {}
    ans = 0
    for score in score_list : 
        score_dict[score] = score_dict.get(score , 0) + 1
    sorted_dict = sorted(score_dict.items(), key = lambda  x: x[1], reverse= True)
    mode_cnt = sorted_dict[0][1]
    for score_key, cnt in sorted_dict : 
        if cnt == mode_cnt : 
            ans = max(score_key, ans)
        else :
            break
        
    print("#{} {}".format(case_num, ans))
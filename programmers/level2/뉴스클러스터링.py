def solution(str1, str2):
    answer = 0

    def make_set(s) :
        s = s.lower()
        res = []
        for i in range(len(s) -1) :
            two_char = s[i : i + 2]
            if two_char.isalpha() :
                res.append(two_char)
        return res
        
    set1 = make_set(str1) 
    set2 = make_set(str2) 
    unique = set(set1 + set2) 

    intersect = 0
    for element in unique :
        cnt_set1 = set1.count(element)
        cnt_set2 = set2.count(element)
        intersect += min(cnt_set1, cnt_set2)

    union = len(set1) + len(set2) - intersect
    if union == 0 :
        return 65536 
    
    ans = int((intersect / union) * 65536)
    
    return (ans)
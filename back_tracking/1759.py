import sys
input = sys.stdin.readline
l, c = map(int, input().split())
words = list(map(str,input().split()))
words.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
answer = []
def backtracking(level, idx) :
    if level == l :
        cnt_v, cnt_c = 0, 0
        for i in range(l) :
            if answer[i] in vowel :
                cnt_v += 1
            else :
                cnt_c += 1
        if cnt_v >= 1 and cnt_c >= 2 :
            print(''.join(answer))
        return
    
    for i in range(idx, c) :
        answer.append(words[i])
        backtracking(level + 1, i + 1)
        answer.pop()
backtracking(0, 0)
# print(words)
#1개 모음, 2개 자음 (최소)
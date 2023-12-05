from collections import Counter
word = list(input())
word.sort()
word_dict = Counter(word)
half_left = ''
half_right = ''
for key in word_dict :
    while word_dict[key] >= 2:    
        half_left += key
        half_right += key
        word_dict[key] -= 2
for key in word_dict : 
    if word_dict[key] == 1 :
        half_left += key
        word_dict[key] -= 1
half_right = half_right[::-1]
total = half_left + half_right
if total != total[::-1] : 
    print('I\'m Sorry Hansoo')
    exit()
print(total)


# aaaabbc
#abbcc : bcacb

#aaabbb

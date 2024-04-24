n = input()
cards = [0 for _ in range(10)]
for num in n :
    num = int(num)
    if num == 6 or num == 9 :
        if cards[6] >= cards[9] :
            cards[9] += 1
        else :
            cards[6] += 1
    else :
        cards[num] += 1
print(max(cards))


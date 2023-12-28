def solution(sequence, k):
    start = end = 0
    answer = [0, len(sequence)]
    total = sequence[0]

    while True:
        if total < k:
            end += 1
            if end == len(sequence): break
            total += sequence[end]
        else:
            if total == k:
                if end - start < answer[1] - answer[0]:
                    answer = [start, end]
            total -= sequence[start]
            start += 1
    return answer

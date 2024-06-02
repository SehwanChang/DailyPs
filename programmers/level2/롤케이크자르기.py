def solution(topping):
    answer = 0
    # 케이크를 공쳥하게 자르는 방법의 수
    left_set = set()
    right_set = set()

    left_count = [0] * len(topping)
    right_count = [0] * len(topping)
    for i in range(len(topping)):
        left_set.add(topping[i])
        left_count[i] = len(left_set)

    for i in range(len(topping) - 1, -1, -1):
        right_set.add(topping[i])
        right_count[i] = len(right_set)

    for i in range(1, len(topping)):
        if left_count[i - 1] == right_count[i]:
            answer += 1

    return answer

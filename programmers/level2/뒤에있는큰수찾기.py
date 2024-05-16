def solution(numbers):
    answer = [-1] * len(numbers)

    stack = []

    for idx in range(len(numbers)):
        #target : 현재 숫자
        target = numbers[idx]
        # stack : index
        while stack and numbers[stack[-1]] < target:
            answer[stack.pop()] = target
        stack.append(idx)
    return answer

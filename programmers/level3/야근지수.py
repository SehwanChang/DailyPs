import heapq


def solution(n, works):
    answer = 0

    if n >= sum(works):
        return 0
    works = [-work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        max_work = heapq.heappop(works)
        max_work += 1
        heapq.heappush(works, max_work)

    for work in works:
        answer += work * work
    return answer
    # 야근 피로도: 야근 시작시점 ~ 남은 일의 작업량 ^2의 합
    # 1시간 작업량 : 1
    # n시간동안 야근 피로도 최소

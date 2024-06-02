def solution(picks, minerals):
    answer = 0
    mineral_set = []
    def calculate(mineral_set, pick) :
        fatigue = 0
        for mineral in mineral_set :
            if pick == 'diamond':
                fatigue += 1
            elif pick == 'iron' :
                if mineral == 'diamond' :
                    fatigue += 5
                else:
                    fatigue += 1
            elif pick == 'stone' :
                if mineral == 'diamond' :
                    fatigue += 25
                elif mineral == 'iron' :
                    fatigue += 5
                else :
                    fatigue += 1
        return fatigue
    tmp = []
    for idx, mineral in enumerate(minerals) :
        if idx % 5 == 0 and idx != 0 :
            mineral_set.append(tmp)
            tmp = []
        
        tmp.append(mineral)
    if tmp :
        mineral_set.append(tmp)
    # print(mineral_set)
    costs = []
    for section in mineral_set :
        cost = [calculate(section, 'diamond'), calculate(section, 'iron'), calculate(section, 'stone')]
        costs.append(cost)
    while len(costs) > sum(picks) :
        costs.pop()
    costs.sort(key=lambda x: x[2], reverse=True)

    for cost in costs:
        if picks[0] > 0:
            answer += cost[0]
            picks[0] -= 1
        elif picks[1] > 0:
            answer += cost[1]
            picks[1] -= 1
        elif picks[2] > 0:
            answer += cost[2]
            picks[2] -= 1

        
        
    return answer
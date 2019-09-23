# 트럭 여러대 강을 가로지르는 1차선 다리를 정해진 순으로 건넘
# 모든 트럭이 다리를 건너려면 몇초 걸리는지?
# 트럭은 1초ㅔ 1씩 움직임 다리길이는 bridge_length, 다리는 무게 weight까지 견딤
# (트럭이 다리를 와전히 오르지 않은 경우, 이트럭의 무게는 고려하지 않음)


def solution(bridge_length, weight, truck_weights):

    answer, ing_weight = 0, 0
    ing = []
    end = []
    while True:
        answer += 1
        if answer == 1:
            ing_weight += truck_weights[0]
            ing.append([truck_weights.pop(0), 0])

        else:
            if not truck_weights:
                next_truck_weight = truck_weights[0]
                if weight > ing_weight + next_truck_weight:
                    ing.append([truck_weights.pop(0), 0])

        for i in ing:
            i[1] += 1

        idx = 0
        while True:
            if ing[idx][1] >= bridge_length:
                tmp = ing.pop(idx)
                idx -= 1
                ing_weight -= tmp[0]
            idx += 1
            if idx >= len(ing):
                break

        if not truck_weights and not ing:
            break


    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))
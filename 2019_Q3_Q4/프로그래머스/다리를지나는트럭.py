# 트럭 여러대 강을 가로지르는 1차선 다리를 정해진 순으로 건넘
# 모든 트럭이 다리를 건너려면 몇초 걸리는지?
# 트럭은 1초에 1씩 움직임 다리길이는 bridge_length, 다리는 무게 weight까지 견딤
# (트럭이 다리를 와전히 오르지 않은 경우, 이트럭의 무게는 고려하지 않음)


def solution(bridge_length, withstand_weight, truck_lst):

    time, bridge_weight = 0, 0
    on_bridge_lst = []
    passed_lst = []

    while True:

        time += 1

        if truck_lst:
            current_truck_weight = truck_lst[0]
            if current_truck_weight + bridge_weight <= withstand_weight:
                bridge_weight += current_truck_weight
                on_bridge_lst.append([truck_lst.pop(0), 0])

        # 다리에 있는 트럭의 대기시간(다리길이) 증가
        for truck_on_bridge in on_bridge_lst:
            truck_on_bridge[1] += 1

        idx = 0
        while True:
            if on_bridge_lst[idx][1] >= bridge_length:
                tmp = on_bridge_lst.pop(idx)
                idx -= 1
                bridge_weight -= tmp[0]
                passed_lst.append(tmp[0])
            idx += 1
            if idx >= len(on_bridge_lst):
                break




        #종료문 설정
        if not truck_lst and not on_bridge_lst:
            break


    return time +1


bridge_length = 2
withstand_weight = 10
truck_lst = [7,4,5,6]


print(solution(bridge_length, withstand_weight, truck_lst))
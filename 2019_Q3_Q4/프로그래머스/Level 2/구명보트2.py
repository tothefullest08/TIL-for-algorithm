# 무인도 구명보트 구출
# 최대 2명만 탈 수 있음. 무게 제한
# 몸무게 배열 people, 무게 제한 limit, 구명보트 갯수 최소값

def rescue(people, limit):

    Q = [people.pop(0)]
    cnt = 0

    while True:
        cnt += 1
        if not people:
            break
        current_weight = Q.pop(0)
        tmp = []
        for i in range(len(people)):
            next_weight = people[i]
            if current_weight + next_weight <= limit:
                tmp.append([i,next_weight])

        if not tmp:
            Q.append(people.pop(0))
        else:
            my_max = [0, 0]
            for sub_tmp in tmp:
                if my_max[1] < sub_tmp[1]:
                    my_max = [sub_tmp[0], sub_tmp[1]]

            people.pop(my_max[0])
            Q.append(people.pop(0))

    return cnt

def solution(people, limit):

    Q = [people.pop(0)]
    cnt = 0

    while True:
        cnt += 1
        if not people:
            break
        current_weight = Q.pop(0)
        tmp = []
        for i in range(len(people)):
            next_weight = people[i]
            if current_weight + next_weight <= limit:
                tmp.append([i, next_weight])

        if not tmp:
            Q.append(people.pop(0))
        else:
            my_max = [0, 0]
            for sub_tmp in tmp:
                if my_max[1] < sub_tmp[1]:
                    my_max = [sub_tmp[0], sub_tmp[1]]

            people.pop(my_max[0])
            Q.append(people.pop(0))

    return cnt


# print(solution([70,50,80,50], 100))
# print(solution([70,80,50], 100))
print(solution([10,20,30,40,50,60,70,80,90], 100))
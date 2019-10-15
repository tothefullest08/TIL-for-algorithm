# 무인도 구명보트 구출
# 최대 2명만 탈 수 있음. 무게 제한
# 몸무게 배열 people, 무게 제한 limit, 구명보트 갯수 최소값


def solution(people, limit):
    people.sort(reverse=True)
    cnt = 0

    while True:
        cnt += 1
        current_weight = people.pop(-1)
        if not people:
            break

        for i in range(len(people)):
            next_weight = people[i]
            if current_weight + next_weight <= limit:
                people.pop(i)
                break

    return cnt

# print(solution([70,50,80,50], 100))
# print(solution([70,80,50], 100))
# print(solution([10,20,30,40,50,60,70,80,90], 100))

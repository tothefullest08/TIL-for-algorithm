# 무인도 구명보트 구출
# 최대 2명만 탈 수 있음. 무게 제한
# 몸무게 배열 people, 무게 제한 limit, 구명보트 갯수 최소값


def solution(people, limit):
    people.sort()
    N = len(people)
    heavy = len(people)-1
    cnt = 0
    light = 0

    while True:
        if people[light] + people[heavy] <= limit:
            cnt += 1
            heavy -= 1
            light += 1

        else:
            heavy -= 1

        if light >= heavy:
            break

    return N - cnt

print(solution([70,50,80,50], 100))
print(solution([70,80,50], 100))
print(solution([10,20,30,40,50,60,70,80,90], 100))

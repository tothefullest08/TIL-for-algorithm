# 무인도 구명보트 구출
# 최대 2명만 탈 수 있음. 무게 제한
# 몸무게 배열 people, 무게 제한 limit, 구명보트 갯수 최소값

def rescue(people, limit, ans):
    Q = [people.pop(0)]
    cnt = 0
    while True:
        cnt += 1
        if not people or ans < cnt:
            break
        current_weight = Q.pop(0)
        next_weight_idx = -1
        for i in range(len(people)):
            next_weight = people[i]
            if current_weight + next_weight <= limit:
                next_weight_idx = i
                break

        if next_weight_idx < 0:
            Q.append(people.pop(0))
        else:
            people.pop(next_weight_idx)
            Q.append(people.pop(0))

    return cnt

def solution(people, limit):
    N = len(people)
    limit = limit

    ans = 987654321
    for i in range(N):
        people_array = [x for x in people]
        sub_ans = rescue(people_array, limit, ans)
        if ans > sub_ans:
            ans = sub_ans

    return ans

print(solution([70,50,80,50], 100))
print(solution([70,80,50], 100))
import sys

sys.stdin = open('2.sprint_trainning.txt', 'r')

# sprint training

def getMostVisited(n, sprints):

    visited = [0]*(n+2) # visited 배열 생성
    for i in range(len(sprints)-1):
        start = min(sprints[i], sprints[i+1]) # 시작 sprint 설정
        goal = max(sprints[i], sprints[i+1]) # 종료 sprint 설정
        visited[start] += 1
        visited[goal+1] -= 1

    sprint_visits_array = [0]*(n+1) # 스프린트별 방문횟수 배열
    tmp = 0
    for i in range(1, n+1):
        tmp += visited[i]
        sprint_visits_array[i] = tmp

    answer = [0, 0] # 최종값 저장. [인덱스. 누적방문값] 순으로 저장
    for i in range(1, n+1):
        if sprint_visits_array[i] > answer[1]:
            answer = [i, sprint_visits_array[i]]

    return answer[0]

n = int(input().strip())

sprints_count = int(input().strip())

sprints = []

for _ in range(sprints_count):
    sprints_item = int(input().strip())
    sprints.append(sprints_item)

result = getMostVisited(n, sprints)
print(result)
import sys, itertools
sys.stdin = open('bj17471_게리맨더링.txt', 'r')

# 선거구를 2개로 나누기.
# 한 선거구에 포함된 구역은 모두 연결되어있어야함.

def inspection(group):
    global N
    visited = [0]*(N+1)
    visited[group[0]] = True
    Q = [group[0]]
    cnt = 1
    while Q:
        now = Q.pop(0)
        for next in range(1, N+1):
            if MyMap[now][next] and next in group and not visited[next]:
                Q.append(next)
                visited[next] = True
                cnt += 1

    if cnt == len(group):
        return True
    return False

N = int(input())
MyMap = [[0] * (N+1) for _ in range(N+1)]

# 노드 별 인구 수를 딕셔너리에 저장
population = {}
tmp = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    population[i] = tmp[i]

# MyMap 찍기
for now in range(1, N+1):
    info_array = list(map(int, input().split()))
    for i in range(1, info_array[0]+1):
        MyMap[now][info_array[i]], MyMap[info_array[i]][now] = 1, 1


# 2분류로 나누기
num = [x for x in range(1, N+1)]
ans = 987654321
for i in range(1, N//2+1):
    for j in list(itertools.combinations(num, i)):
        print(j)
        # 그룹 나누기
        group1 = list(j)
        group2 = []
        for k in num:
            if k not in group1: group2.append(k)

        # 연결 검증
        if inspection(group1) and inspection(group2):
            group1_sum, group2_sum = 0, 0
            for sub_num in group1:
                group1_sum += population[sub_num]

            for sub_num in group2:
                group2_sum += population[sub_num]

            sub_ans = abs(group1_sum - group2_sum)

            if sub_ans < ans:
                ans = sub_ans

if ans != 987654321:
    print(ans)
else:
    print(-1)



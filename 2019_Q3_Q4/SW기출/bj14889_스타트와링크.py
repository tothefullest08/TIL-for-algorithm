import sys
sys.stdin = open('bj14889_스타트와링크.txt', 'r')

import itertools

# N명의 사람들이 모임 (항상 짝수)


def check(team):
    global result

    start_team = team
    link_team = []
    for i in people_lst:
        if i not in team:
            link_team.append(i)

    start_team_permu = list(itertools.permutations(start_team, 2))
    link_team_permu = list(itertools.permutations(link_team, 2))

    start_team_ability, link_team_ability = 0, 0
    for i in start_team_permu:
        y, x = i[0], i[1]
        start_team_ability += MyMap[y][x]

    for i in link_team_permu:
        y, x = i[0], i[1]
        link_team_ability += MyMap[y][x]

    sub_result = abs(start_team_ability - link_team_ability)

    if sub_result < result:
        result = sub_result





N = int(input())
MyMap = [list(map(int, input().split())) for i in range(N)]
people_lst = [i for i in range(N)]


combi_lst = list(itertools.combinations(people_lst, N//2))
result = 987654321

for i in combi_lst:
    check([*i])

print(result)



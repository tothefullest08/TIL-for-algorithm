# 최대 10개의 메세지 처리하는 메세지 큐가 있음
# 메세지 큐에 메세지가 쌓이면 이를 순차적으로 최대 10개의 컨슈머가 처리함
# 메세지마다 처리에 걸리는 시간은 다를 수 있고, 하나의 메세지 처리에 걸리는 시간은 최대 100초이다
# 모든 메세지가 0초에 도착ㅇ하고 입력받는 순서대로 처리한다고 가정했을 떄, 전체 메세지를 처리하는데 걸리는 시간 계산

import sys
sys.stdin = open('메세지처리시간.txt', 'r')

N, people = map(int, input().strip().split(' '))
messages = [int(input()) for _ in range(N)]

array = []
for i in range(people):
    array.append([])

for i in range(people):
    array[i].append(messages.pop(0))

time = 0
ans = []
while True:
    time += 1
    for i in range(people):
        if array[i]:
            array[i][0] -= 1
            if array[i][0] == 0:
                ans.append(array[i].pop(0))
                if messages:
                    array[i].append(messages.pop(0))

    if len(ans) == N:
        break

print(time)

con=[0]*n
for i in staticmethod:
    i = con.index(min(con))
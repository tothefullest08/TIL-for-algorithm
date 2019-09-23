import sys, itertools
sys.stdin = open('2383_점심식사시간.txt', 'r')

# N * N 정사격형 모양 사람들
# 점심 먹기위해 아래층 내려가야함. 빨리 먹기 위해 최대한 빠른 시간 내 내려가야함
# 방안의 사람들: P // 계단 입구: S
# 이동 완료 시간: 모든 사람들이 계단을 내려가 아래층으로 이동 완료한 시간
# 이동 시간: 1) 계단입구까지 이동 시간 + 2) 계단을 내려가는 시간
# 1) abs(사람위치 - 계단위치)
# 2) 계단 입구 도착 => 1분후 아랫칸
# 2-1) 계단에는 3명만 올라갈 수 있음
# 2-2) 3명이 계단 내려갈 경우, 1명이 계단을 완전히 내려갈때 까지 계단 입구 대기
# 2-3) 계단 길이 K, 계단이 올라간 후 내려가는데 k분 걸림


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    MyMap = [list(map(int, input().split())) for _ in range(N)]

    people_lst = []
    for y in range(N):
        for x in range(N):
            if MyMap[y][x] == 1:
                people_lst.append([y,x])


    print(people_lst)



import sys
sys.stdin = open('bj15685_드래곤커브.txt', 'r')


N = int(input())
MyMap = [[0]*101 for _ in range(101)]
#우, 상, 좌, 하
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

for _ in range(N):
    #시작좌표, 방향, 세대
    start_x, start_y, dir, gen = map(int, input().split())
    dir_lst = [0]
    dir_lst[0] = dir


    #방향 리스트 설정

    #세대별 반복
    for i in range(gen):
        #점화식은 배열의 마지막값(j)부터 역으로 접근하여, (j+1)%4를 하면 됨
        # 0 -> 1 / 1 -> 2 / 2 -> 3 / 3 -> 0
        for j in range(len(dir_lst)-1, -1, -1):
            dir_lst.append((dir_lst[j]+1) % 4)

    #맵 찍기
    MyMap[start_y][start_x] = 1
    for dir in dir_lst:
        start_y += dy[dir]
        start_x += dx[dir]
        MyMap[start_y][start_x] = 1


#1x1 정사각형 갯수 카운팅

ans = 0
for y in range(100):
    for x in range(100):
        if MyMap[y][x] == 1:
            if MyMap[y][x] and MyMap[y+1][x] and MyMap[y][x+1] and MyMap[y+1][x+1]:
                ans += 1

# #우 하 좌 상 (inspection용 dy, dx)
# i_dy = [0, 1, 0, -1]
# i_dx = [1, 0, -1, 0]
#
# ans = 0
# for y in range(100):
#     for x in range(100):
#         if MyMap[y][x] == 1:
#             selected_y, selected_x = y, x
#             cnt = 0
#             for dir in range(4):
#                 if MyMap[selected_y + i_dy[dir]][selected_x + i_dx[dir]] == 1:
#                     selected_y += i_dy[dir]
#                     selected_x += i_dx[dir]
#                     cnt += 1
#             if cnt == 4 and y == selected_y and x == selected_x:
#                 ans += 1
#
print(ans)






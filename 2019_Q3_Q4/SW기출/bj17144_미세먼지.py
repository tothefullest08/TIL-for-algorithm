import sys
sys.stdin = open('bj17144_미세먼지.txt', 'r')

def IsSafe(y,x):
    return 0<=y<Y and 0<=x<X

def spread():
    dust_to_be_added = []
    while Q:
        y,x = Q.pop(0)
        dust = MyMap[y][x] // 5
        for dir in range(4):
            n_y = y + dy[dir]
            n_x = x + dx[dir]
            if IsSafe(n_y, n_x) and MyMap[y][x] != -1 and MyMap[n_y][n_x] != -1:
                dust_to_be_added.append([n_y, n_x, dust])
                MyMap[y][x] -= dust
    for new_dust in dust_to_be_added:
        MyMap[new_dust[0]][new_dust[1]] += new_dust[2]

def clean(y, x, prev_value):
    visited[y][x] = 1

    if path1[y][x] == -1:
        return
    for dir in range(4):
        n_y = y + dy1[dir]
        n_x = x + dx1[dir]
        if IsSafe(n_y, n_x) and path1[n_y][n_x] == 1 and not visited[n_y][n_x]:
            next_dust_lst.append([n_y, n_x, MyMap[y][x]])
            clean(n_y, n_x, MyMap[y][x])
            break

def clean1(y, x, prev_value):
    visited[y][x] = 1
    if path2[y][x] == -1:
        return
    for dir in range(4):
        n_y = y + dy1[dir]
        n_x = x + dx1[dir]
        if IsSafe(n_y, n_x) and path2[n_y][n_x] == 1 and not visited[n_y][n_x]:
            next_dust_lst.append([n_y, n_x, MyMap[y][x]])
            clean1(n_y, n_x, MyMap[y][x])
            break


Y,X,T = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(Y)]

#상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

#우 상 좌 하
dy1 = [0, -1, 0, 1]
dx1 = [1, 0, -1, 0]

#우 하 좌 상
dy2 = [0, 1, 0, -1]
dx2 = [1, 0, -1, 0]

#청소기 위치
cleaner_lst = []
for y in range(Y):
    if MyMap[y][0] == -1:
        cleaner_lst.append([y, 0])
cleaner1_y, cleaner2_y  = cleaner_lst[0][0], cleaner_lst[1][0]

#청소기 루트 표시
path1 = [[0] * X for _ in range(Y)]
path2 = [[0] * X for _ in range(Y)]

for y in range(cleaner1_y+1): path1[y][0], path1[y][-1] = 1, 1
for y in range(cleaner2_y, Y): path2[y][0], path2[y][X-1] = 1, 1
for x in range(X):
    path1[cleaner1_y][x], path2[cleaner2_y][x] = 1, 1
    path1[0][x], path2[-1][x] = 1,1
path1[cleaner1_y][0], path2[cleaner2_y][0] = -1, -1


#확산가능한 먼지
for i in range(T):
    Q = []
    visited = [[0] * X for _ in range(Y)]
    next_dust_lst = [[cleaner1_y, 1, 0], [cleaner2_y, 1, 0]]

    for y in range(Y):
        for x in range(X):
            if MyMap[y][x] >= 5:
                Q.append([y,x])

    spread()
    clean(cleaner1_y, 1, -1)
    clean1(cleaner2_y, 1, -1)

    for i in next_dust_lst:
        MyMap[i[0]][i[1]] = i[2]


ans = 0
for y in range(Y):
    for x in range(X):
        if MyMap[y][x] > 0:
            ans += MyMap[y][x]

print(ans)


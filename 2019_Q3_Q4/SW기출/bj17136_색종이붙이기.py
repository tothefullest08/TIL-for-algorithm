import sys
sys.stdin = open('bj17136_색종이붙이기.txt', 'r')

def IsSafe(y,x):
    return 0<=y<10 and 0<=x<10 and MyMap[y][x] == -1

def Check(size, y, x):
    for n_y in range(y, y+size):
        for n_x in range(x, x+size):
            if not IsSafe(n_y, n_x):
                return False
    return True

def attach(size, y, x):
    for n_y in range(y, y+size):
        for n_x in range(x, x+size):
           MyMap[n_y][n_x] = size

def dettach(size, y, x):
    for n_y in range(y, y+size):
        for n_x in range(x, x+size):
           MyMap[n_y][n_x] = 1



N = 10
MyMap = [list(map(int, input().split())) for _ in range(N)]

for y in range(10):
    for x in range(10):
        if MyMap[y][x] == 1:
            MyMap[y][x] = -1

cnt = 0
flag = False
life = [0, 5, 5, 5, 5, 5]
for i in range(5, 0, -1):
    for y in range(N):
        for x in range(N):
            if MyMap[y][x] == 1 and life[i] > 0:
                if Check(i, y, x):
                    attach(i, y, x)
                    cnt += 1
                    life[i] -= 1


flag = False

for y in range(N):
    for x in range(N):
        if MyMap[y][x] == 1:
            print(-1)
            flag = True
            break
    if flag:
        break

if not flag:
    print(cnt)
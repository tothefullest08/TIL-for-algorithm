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
    global attached_so_far

    for n_y in range(y, y+size):
        for n_x in range(x, x+size):
           MyMap[n_y][n_x] = size
           attached_so_far += 1


def dettach(size, y, x):
    global attached_so_far

    for n_y in range(y, y+size):
        for n_x in range(x, x+size):
           MyMap[n_y][n_x] = -1
           attached_so_far -= 1

def DFS(life, sub_result):
    global result, attached_so_far

    if sub_result > result or attached_so_far > total_paper:
        return

    for y in range(N):
        for x in range(N):
            if MyMap[y][x] == -1:
                for paper in range(5,0,-1):
                    if Check(paper, y, x) and life[paper] > 0:
                        attach(paper, y, x)
                        life[paper] -= 1
                        DFS(life, sub_result+1)
                        dettach(paper, y, x)
                        life[paper] += 1
                return

            if y == N-1 and x == N-1:
                if sub_result < result:
                    result = sub_result
                return

N = 10
MyMap = [list(map(int, input().split())) for _ in range(N)]

total_paper = 0
attached_so_far = 0
for y in range(10):
    for x in range(10):
        if MyMap[y][x] == 1:
            MyMap[y][x] = -1
            total_paper += 1

result, sub_result = 987654321, 0

life = [0, 5, 5, 5, 5, 5]
DFS(life, sub_result)


if result != 987654321:
    print(result)
else:
    print(-1)

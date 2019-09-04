import sys
sys.stdin = open('bj15684_사다리조작.txt','r')


def check():
    for x in range(X):
        goal = x
        for y in range(Y):
            if MyMap[y][goal]:
                goal += 1
            elif MyMap[y][goal-1]:
                goal -= 1
        if goal != x: return False
    return True

def DFS(idx, cnt):
    global ans

    if cnt == min_cnt:
        if check():
            ans = cnt
        return
    for y in range(idx, Y):
        for x in range(X-1):
            if not MyMap[y][x] + MyMap[y][x-1] + MyMap[y][x+1]:
                MyMap[y][x] = 1
                DFS(y, cnt+1)
                MyMap[y][x] = 0


X, ladder_num, Y = map(int, input().split())
MyMap = [[0] * X for _ in range(Y)]

for _ in range(ladder_num):
    y, x = map(int, input().split())
    MyMap[y-1][x-1] = 1

ans = 987654321

for min_cnt in range(4):
    DFS(0, 0)
    if ans != 987654321:
        print(ans)
        break
else:
    print(-1)
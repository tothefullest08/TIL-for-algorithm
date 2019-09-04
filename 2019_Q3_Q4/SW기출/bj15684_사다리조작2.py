import sys
sys.stdin = open('bj15684_사다리조작.txt','r')

def DFS(idx, cnt):
    global ans
    if cnt == min_cnt:
        if check():
            ans = cnt
        return
    for y in range(idx, Y+1):
        for x in range(1, X):
            if not MyMap[y][x] + MyMap[y][x-1] + MyMap[y][x+1]:
                MyMap[y][x] = 1
                DFS(idx, cnt+1)
                MyMap[y][x] = 0

def check():
    for x in range(1, X+1):
        goal = x
        for y in range(1, Y+1):
            if MyMap[y][goal]:
                goal += 1
            elif MyMap[y][goal-1]:
                goal -= 1
        if goal != x: return False
    return True

X, ladder_num, Y = map(int, input().split())
MyMap = [[0] * 11 for _ in range(31)]

for _ in range(ladder_num):
    y, x = map(int, input().split())
    MyMap[y][x] = 1

ans = 987654321

for min_cnt in range(4):
    DFS(1, 0)
    if ans != 987654321:
        print(ans)
        break
else:
    print(-1)
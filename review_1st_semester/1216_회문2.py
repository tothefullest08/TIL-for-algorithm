import sys
sys.stdin = open('1216_회문2.txt', 'r')


for tc in range(1, 2):
    tc = int(input())
    N = 5
    Table = [0]*5
    for i in range(N):
        Table[i] = list(map(int, input().split()))

    print(Table)

    for y in range(N):
        for x in range(N):
            if y > x:
                Table[y][x], Table[x][y] = Table[x][y], Table[y][x]

    print(Table)

import sys

sys.stdin = open("4836_색칠하기.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    red_lst = []
    blue_lst = []
    for i in range(N):
        y1, x1, y2, x2, color = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if color == 1:
                    red_lst.append((y,x))
                elif color == 2:
                    blue_lst.append((y,x))

    result = []
    if len(red_lst) > len(blue_lst):
        for i in blue_lst:
            if i in red_lst:
                result.append(i)

    if len(red_lst) < len(blue_lst):
        for i in red_lst:
            if i in blue_lst:
                result.append(i)

    print('#%s %d'%(tc, len(result)))
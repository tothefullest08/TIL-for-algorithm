import sys
sys.stdin = open('1247_최적경로.txt', 'r')

def DFS(x,y, cnt):
    global result, sub_result

    if sub_result > result:
        return

    if cnt == N:
        sub_result += abs(end_x - x) + abs(end_y - y)
        if sub_result < result:
            result = sub_result
        sub_result -= abs(end_x - x) + abs(end_y - y)
        return


    for i in range(N):
        if not visited_y[i]:
            sub_result += abs(x - client_lst[i][0]) + abs(y - client_lst[i][1])
            visited_y[i] = 1
            DFS(client_lst[i][0], client_lst[i][1], cnt+1)
            sub_result -= abs(x - client_lst[i][0]) + abs(y - client_lst[i][1])
            visited_y[i] = 0


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    base_lst = list(map(int, input().split()))
    start_x, start_y = base_lst[0], base_lst[1]
    end_x, end_y = base_lst[2], base_lst[3]
    client_lst = []
    for i in range(2, N+2):
        client_lst.append([base_lst[i*2], base_lst[i*2+1]])
    # print(client_lst)

    visited_y = [0] * N
    result, sub_result = 987654321, 0
    DFS(start_x, start_y, 0)
    print('#%d %d'%(tc, result))
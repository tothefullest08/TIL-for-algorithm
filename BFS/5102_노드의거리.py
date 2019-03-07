import sys
sys.stdin = open('5102_노드의거리.txt', 'r')


def BFS(start):
    global result
    Q.append(start)
    visited[start] = 1

    while Q:
        start = Q.pop(0)
        for next in range(v+1):
            if MyMap[start][next] and not visited[next]:
                Q.append(next)
                visited[next] = 1
                distance[next] = distance[start] + 1
                if next == end_node:
                    result = distance[next]
                    return


TC = int(input())
for tc in range(1, TC+1):
    v, e = map(int, input().split())
    MyMap = [[0]*(v+1) for _ in range(v+1)]
    for i in range(e):
        start, end = map(int, input().split())
        MyMap[start][end] = 1
        MyMap[end][start] = 1

    start_node, end_node = map(int, input().split())
    distance = [0]*(v+1)
    visited = [0]*(v+1)
    Q = []
    result = 0
    BFS(start_node)
    print('#%d %d'%(tc, result))

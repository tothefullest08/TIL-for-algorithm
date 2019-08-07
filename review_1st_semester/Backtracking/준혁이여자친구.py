import sys
sys.stdin = open('준혁이여자친구.txt','r')

def DFS(start):
    global result, final_result

    if start == v:
        if final_result > result:
            final_result = result
        return

    for next in range(1, v+1):
        if MyMap[start][next] and not visited[next]:
            result += MyMap[start][next]
            visited[next] = 1
            DFS(next)
            result -= MyMap[start][next]
            visited[next] = 0






v, e = map(int, input().split())
MyMap = [[0] * (v + 1) for _ in range(v + 1)]

for i in range(e):
    start, end, cost = map(int, input().split())
    MyMap[start][end] = cost


visited = [0] * (v+1)
result = 0
final_result = 987654321
DFS(1)

print(MyMap)
print(final_result)

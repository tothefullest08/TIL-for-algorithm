import sys
sys.stdin = open('예산관리.txt', 'r')

def DFS(x):
    print(result)
    if sum(result) > Budget:
        return

    final_result.append(sum(result))

    for i in range(N):
        if cost[i] not in visited:
            visited.append(cost[i])
            result.append(cost[i])
            DFS(x+1)
            visited.remove(cost[i])
            result.remove(cost[i])


Budget = int(input())
N = int(input())
cost = list(map(int, input().split()))
visited = []
result, final_result = [], []
DFS(0)
# print(final_result)
print(max(final_result))

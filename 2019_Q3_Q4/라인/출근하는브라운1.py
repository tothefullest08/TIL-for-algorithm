import sys
sys.stdin = open('출근하는브라운.txt', 'r')

#다른 사람들과 최대한 멀리 떨어져 앉을때 가장 가까운 사람과의 거리를 구하라

N = int(input())
seats = [int(x) for x in input().split()]
distance = [999999999] * N
ans = 0
for i in range(N):
    if not seats[i]:
        visited = [0] * N
        Q = [[i,0]]
        visited[i] = 1
        while Q:
            current_seat, dis = Q.pop(0)
            if seats[current_seat] and dis < distance[i]:
                distance[i] = dis
                break
            if current_seat -1 >= 0 and not visited[current_seat-1]:
                visited[current_seat-1] = 1
                Q.append([current_seat-1, dis+1])
            if current_seat +1 < N and not visited[current_seat+1]:
                visited[current_seat+1] = 1
                Q.append([current_seat+1, dis+1])

for j in distance:
    if j == 999999999:
        continue
    elif j > ans:
        ans = j

print(str(ans))

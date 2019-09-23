import sys
sys.stdin = open('출근하는브라운.txt', 'r')

#다른 사람들과 최대한 멀리 떨어져 앉을때 가장 가까운 사람과의 거리를 구하라

N = int(input())
seats = list(map(int, input().split()))

left_array = []
right_array = []
for i in range(N):
    if seats[i] == 1:
        left_array.append(0)
    else:
        cnt = 0
        for j in range(i, -1, -1):
            if seats[j] == 1:
                left_array.append(cnt)
                break
            else:
                cnt += 1

for i in range(N):
    if seats[i] == 1:
        right_array.append(0)
    else:
        cnt = 0
        for j in range(i, N):
            if seats[j] == 1:
                right_array.append(cnt)
                break
            elif seats[j] != 1 and cnt != N-i:
                cnt += 1
        if cnt == N-i:
            right_array.append(cnt)

# 1 0 0 0 0

ans = 0
for i in list(zip(left_array, right_array)):
    if ans < min(i) != 0:
        ans = min(i)

print(left_array)
print(right_array)
print(ans)



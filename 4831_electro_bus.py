import sys
sys. stdin = open('4831_electro_bus.txt','r')

TC = int(input())
for tc in range(1, TC+1):
    K,N,M = map(int,input().split())
    station = list(map(int, input().split()))
    station_lst = [0] * (N+1)

    for i in range(len(station)):
        station_lst[station[i]] += 1

    start = 0
    end = K
    cnt = 0

    while True:
        zero = 0
        for i in range(start+1, end+1):
            if station_lst[i] == 1:
                start = i

            else:
                zero += 1

        if zero == K:
            cnt = 0
            break

        cnt += 1
        end = start + K

        if end >= N:
            break

    print('#%s %d'%(tc, cnt))





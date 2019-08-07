import sys
sys.stdin = open('15650_N과M_2.txt')

def Combi(start):
    if start == M:
        tmp = [0]*M
        for i in range(M):
            tmp[i] = Data[result[i]]
        print(*tmp)
        return

    for i in range(N):
        if index_fuel[i] > 0:
            if start > 0:
                if result[start-1] > i:
                    continue
            index_fuel[i] -= 1
            result[start] = i
            Combi(start+1)
            index_fuel[i] += 1


N, M = map(int, input().split())
Data = [x for x in range(1, N+1)]
index_fuel = [1]*N
result = [0]*M
Combi(0)

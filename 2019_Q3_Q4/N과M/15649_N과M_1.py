import sys
sys.stdin = open('15649_N과M_1.txt')

def permu(start):

    if start == M:
        print(*result)
        return

    for i in range(N):
        if index_fuel[i] > 0:
            index_fuel[i] -= 1
            result[start] = Data[i]
            permu(start+1)
            index_fuel[i] += 1


N, M = map(int, input().split())
Data = [x for x in range(1, N+1)]
index_fuel = [1]*N
result = [0]*M

permu(0)
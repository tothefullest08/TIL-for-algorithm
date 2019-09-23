import sys
sys.stdin = open('k번째순열찾기.txt', 'r')

#123으로 만들 순열 중 오름차순으로 정렬했을 때 3번째 순열은 213이다
#첫번째 행에 공백을 구분자로 숫자가 주어짐

numbers = list(map(int, input().split()))
N = len(numbers)
find_idx = int(input())-1
numbers.sort()

def permu(start):
    global idx, ans
    if start == N:
        idx += 1
        if idx == find_idx:
            for i in result:
                ans += str(i)
            print(int(ans))
        return

    for i in range(N):
        if index_fuel[i] > 0:
            index_fuel[i] -= 1
            result[start] = numbers[i]
            permu(start+1)
            if ans:
                return
            index_fuel[i] += 1

idx = -1
index_fuel = [1] * N
result = [0] * N
ans = ''
permu(0)


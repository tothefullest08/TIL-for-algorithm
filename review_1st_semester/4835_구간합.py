# 10 3
# 1 2 3 4 5 6 7 8 9 10

# length, rng = map(int, input().split())

import sys

sys. stdin = open('4835_구간합.txt','r')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))

    lst = []
    for i in range(N-M+1):
        lst.append(sum(Data[i:i+M]))

    print('#%s %d'%(tc, max(lst)-min(lst)))

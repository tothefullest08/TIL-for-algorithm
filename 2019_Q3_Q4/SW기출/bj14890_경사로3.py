import sys
sys.stdin = open('bj14890_경사로.txt','r')

import itertools

N, L = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    print(MyMap[y][:])
print()

Map=list(map(list,zip(*MyMap[:])))
Map2=list(zip(*MyMap[:]))
Map3=list(zip(MyMap[:]))

for y in range(N):
    print(Map[y][:])

print('-------')
for y in range(N):
    print(Map2[y][:])

print('-------')
for y in range(N):
    print(Map3[y][:])

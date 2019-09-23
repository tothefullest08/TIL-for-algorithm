import itertools
from collections import deque


num = [1,2,3,4,5]

print("순열")
print(list(itertools.permutations(num,2)))
print("------")
print("중복순열")
print(list(itertools.product(num, repeat=2)))
print("------")
print("조합")
print(list(itertools.combinations(num,2)))
print("------")
print("중복조합")
print(list(itertools.combinations_with_replacement(num,2)))

print("------")
MyMap = [[1,2,3],[4,5,6],[7,8,9]]
for y in MyMap:
    print(y)
print("맵돌리기")
MyMap = list(map(list, zip(*MyMap[::-1])))
for y in MyMap:
    print(y)

MyMap = [[1,5,4], [6, 9, 1], [15, 10, 3]]
print("------")
print("람다")
MyMap.sort(key=lambda x:x[2], reverse = True)
print(MyMap)


print("------")
print("뎈")
Q = deque()
Q.append(1)
print(Q)
Q.popleft()
print(Q)


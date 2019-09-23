import itertools

num = [1,2,3,4]


print('순열' , list(itertools.permutations(num, 2)))
print('조합' , list(itertools.combinations(num, 2)))

print('중복순열,' , list(itertools.product(num,repeat=2)))
print('중복조합', list(itertools.combinations_with_replacement(num,2)))

x_array = [1,2,3,4,5]
MyMap = [x_array for _ in range(5)]

for y in MyMap:
    print(y)


print(list(map(list, zip(*MyMap))))

array = [[1,2,3],[10,11,12], [7,8,9], [4,5,6]]
array.sort(key=lambda x:x[2])
print(array)

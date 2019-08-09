import itertools

num = [1,2,3,4]
result = list(itertools.combinations_with_replacement(num,4))
print(result)
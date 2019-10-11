def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))

print("'333' > '3130'")
if '333' > '3':
    print(True)
else:
    print(False)
print('=======')

print("'333' > '3330'")
if '333' > '3330':
    print(True)
else:
    print(False)

print(ord('3'))
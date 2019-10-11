def solution(numbers):
    numbers = [str(x) for x in numbers]

    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if numbers[j] + numbers[j + 1] < numbers[j + 1] + numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    answer = ''.join(numbers)
    return answer



print(solution([3, 30, 34, 5, 9]))




def solution(x):
    str_x = str(x)
    my_sum = 0
    for i in str_x :
        my_sum += int(i)

    answer = False
    if not x % my_sum:
        answer = True
    return answer

print(solution(11))







# 이진수 변환 함수
def binary(num):
    ans = ''
    mok, nam = 0, 0
    while True:
        mok = num // 2
        nam = num % 2

        ans = str(nam) + ans
        num = mok

        if mok == 0:
            break
    return ans

# 검사 함수
def inspection(num):
    array = []
    for i in range(len(num)):
        if num[i] == '1':
            array.append(i)


    if len(array) == 1:
        return 0
    else:
        ans = 0
        for i in range(len(array)-1):
            sub_ans = array[i+1] - array[i]
            if sub_ans > ans:
                ans = sub_ans

        return ans - 1


def solution(N):
    # write your code in Python 3.6
    bi_num = binary(N)
    ans = inspection(bi_num)
    return ans

print(solution(1041))
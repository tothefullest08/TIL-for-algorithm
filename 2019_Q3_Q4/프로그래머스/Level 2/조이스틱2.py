def find_from_front(letter_base, letter_to_be_found):
    cnt = 0
    if letter.index(letter_to_be_found) < letter.index(letter_base):
        cnt = len(letter) - letter.index(letter_base) + letter.index(letter_to_be_found) + 1
    elif letter.index(letter_to_be_found) > letter.index(letter_base):
        cnt = letter.index(letter_to_be_found) - letter.index(letter_base)
    else:
        cnt = 0

    return cnt

def find_from_back(letter_base, letter_to_be_found):
    cnt = 0
    if letter.index(letter_to_be_found) < letter.index(letter_base):
        cnt = letter.index(letter_base) - letter.index(letter_to_be_found)
    elif letter.index(letter_to_be_found) > letter.index(letter_base):
        cnt = letter.index(letter_base) + len(letter) - letter.index(letter_to_be_found) + 1
    else:
        cnt = 0
    return cnt

def solution(name):
    answer = 0
    letter_lst = ['A']
    for i in name:
        tmp = min(find_from_front(letter_lst[-1], i), find_from_back(letter_lst[-1], i))
        if len(letter_lst) > 1:
            tmp2 = min(find_from_front(letter_lst[-2], i), find_from_back(letter_lst[-2], i)) + 1
            if tmp2 < tmp:
                tmp = tmp2

        answer += tmp
        letter_lst.append(i)
    return answer


# name = "JEROEN"
name = "JAN"

letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(solution(name))

#각 글자별로

# 앞으로 갈 경우: 찾는 알파벳 인덱스  - 현재 알파벳 인덱스
# 뒤로 갈 경우:  현재 알파벳 인덱스  + 전체길이(N) - 찾는 알파벳 인덱스 + 1
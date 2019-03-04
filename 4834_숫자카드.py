# 3
# 5
# 49679
# 5
# 08271
# 7797946543
# 10

import sys
sys. stdin = open('4834_숫자카드.txt','r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = input()
    Data = [int(_) for _ in Data]
    cnt_lst = [0]*10

    for i in range(N):
        cnt_lst[Data[i]] += 1

    max_index, max_num = 0, 0
    for i in range(len(cnt_lst)-1,-1,-1):
        if cnt_lst[i] > max_index:
            max_index = cnt_lst[i]
            max_num = i

    print('#%s %d %d'%(tc, max_num, max_index))










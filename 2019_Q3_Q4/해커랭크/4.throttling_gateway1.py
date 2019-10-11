import sys

sys.stdin = open('4.throttling_gateway.txt', 'r')

from collections import Counter


def droppedRequests(requestTime):
    requestTime.sort()
    seta = set(requestTime)
    dict1 = {}
    count1 = total = step = 0
    initial_10 = requestTime[0] // 10
    initial_60 = requestTime[0] // 60
    dict1 = Counter(requestTime)
    flag = 0
    # for val in seta:
    #     dict1[val] = requestTime.count(val)

    for key in sorted(dict1):
        value = dict1[key]
        if value > 3:
            count1 += (value - 3)

        if key // 10 != initial_10:
            if step > 20:
                count1 += (step - 20)

            initial_10 = key // 10
            total += step
            step = 0
            flag = 1

        if key // 60 != initial_60:
            if total > 60:
                count1 += (total - 60)

            initial_60 = key // 60
            total = 0
        #            flag=1

        if (flag == 0):
            step += value

        flag = 0

    if step > 20:
        count1 += step - 20
        print("ssdd")
        print(step)
    if total > 60:
        count1 += total - 60
    return count1


N = int(input())
requestTime = [int(input()) for _ in range(N)]
print(droppedRequests(requestTime))
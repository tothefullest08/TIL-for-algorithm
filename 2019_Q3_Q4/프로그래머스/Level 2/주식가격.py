def solution(prices):
    N = len(prices)
    answer = [-1] * N

    for i in range(N):
        current_prices = prices[i]
        for j in range(i, N):
            if current_prices <= prices[j]:
                answer[i] += 1
            elif current_prices > prices[j]:
                answer[i] = j-i
                break

    print(answer)



    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
N = len(prices)


# answer = [4, 3, 1, 1, 0]



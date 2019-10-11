import sys

sys.stdin = open('3.string_chain.txt', 'r')


def longestChain(words):

    word_dict = {} # 단어 별 딕셔너리 배열 생성
    words.sort(key=lambda x: len(x)) # 길이가 짧은 순으로 정렬
    for word in words:
        word_dict[word] = 1 # 각 단어별로 체인 초기값 1 적용
        for i in range(len(word)): # 단어를 분해하기
            sub_word = word[:i] + word[i+1:]  # 슬라이싱을 i까지로 적용하여 한단계 낮은 단어로 분해시킨 후 sub_word에 저장
            if sub_word in word_dict: # 분해시킨 단어가 단어 딕셔너리 배열에 존재할 경우
                # 현재단어의 체인값과 분해시킨단어의 체인값 +1을 비교하여 저장
                word_dict[word] = max(word_dict[word], word_dict[sub_word]+1)

    return max(word_dict.values())

words_count = int(input().strip())

words = []

for _ in range(words_count):
    words_item = input()
    words.append(words_item)

result = longestChain(words)
print(result)


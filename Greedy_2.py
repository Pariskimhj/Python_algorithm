#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 문제 출처 : 이것이 코딩 테스트다

# [1이 될 때까지]

# 어떤 수 N이 아래의 방법을 사용해서 1이 될 때까지의 최소횟수
# 1. N에서 1을 뺀다.
# 2. N이 K로 나누어떨어질 때는 N을 K로 나눈다.

# [입력]
# 첫 줄에 N과 K이 주어짐

# [출력]
# 최소 횟수 출력

# <그리디 알고리즘>

# [1이 될 때까지 문제 풀이]
# N이 1이 되기 전까지 K로 N을 최대한 많이 나눌 수 있도록 하는 것이 최적의 해를 보장

N, K = map(int, input().split()) # N, K 입력 받기
count = 0                        # count 초기화
while N != 1:                    # N이 1이 될때까지 무한루프
    if N % K == 0:               # N이 K의 배수일 때
        N /= K                   # N은 N을 K로 나눈 값으로 변경
        count += 1               # 실행 횟수 1회 추가
    else:                        # N이 K의 배수가 아닐 때
        N -= 1                   # N은 기존 N에 1을 뺀 값으로 변경
        count += 1               # 실행 횟수 1회 추가
print(count)                     # 실행 횟수 출력


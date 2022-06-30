#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 문제 출처 : 이것이 코딩 테스트다

# [숫자 카드 게임]

# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

# 1. 숫자가 쓰인 카드들이 N * M 형태로 놓여있다. N은 행의 개수, M은 열의 개수
# 2. 뽑고자 하는 카드가 포함되어 있는 행 선택
# 3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑는다.
# 4. 처음에 카드를 골라낼 행을 선택할 때 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략세우기

# [입력]
# 첫 줄에 N과 M이 주어짐
# 두번째 줄에 N개 줄에 카드에 적힌 숫자가 주어짐

# [출력]
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

# <그리디 알고리즘>

# [숫자 카드 게임 문제 풀이]
# 행 별로 가장 숫자가 작은 카드 추출, 이 카드 중 가장 큰 숫자가 적힌 카드 추출

# N, M 입력 받기
N, M = map(int, input().split())

# N줄의 card 입력 받기
cards = [map(int, input().split()) for _ in range(N)]

# 각 행 별로 가장 작은 값을 list에 저장 후 list에서 가장 큰 값 출력
print(max([min(card) for card in cards]))

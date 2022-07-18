#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 문제 출처 : 프로그래머스

# [직사각형 별찍기]

# [문제 설명]

# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

# [제한 조건]

# n과 m은 각각 1000 이하인 자연수입니다.

# [예시]

# [입력]

# 5 3

# [출력]

# *****
# *****
# *****

# [나의 풀이]
n, m = map(int, input().strip().split(' '))  # n, m 입력 받아서 정수로 변환
for _ in range(m):                           # m번
    print('*'*n)                             # 별(*) n개 출력


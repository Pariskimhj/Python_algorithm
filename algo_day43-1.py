#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 문제 출처 : SW Expert Academy

# 턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

# [제약 사항]

# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.

# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.

# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
    
for t in range(int(input())): # T 입력 받기
    s = input()               # 문자열 입력 받기
    length = [l for l in range(1, 11) if s[0:l] == s[l:l+l]] # 같은 길이의 구간별로 나눠서 문자열을 서로 비교했을 때 같으면 길이를 리스트에 저장
    print(f"#{t+1} {min(length)}") # 패턴 길이의 최소값 출력


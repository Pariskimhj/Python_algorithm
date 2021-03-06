#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 문제 출처 : SW Expert Academy

# 숫자는 다양성을 가지고 있다. 다양성이란, 숫자를 구성하는 수의 종류를 의미한다.
# 예를 들어서 1512 라는 숫자는 ‘1’, ‘5’, ‘2’로 구성되어 있기 때문에 다양성이 3이다.
# 숫자가 주어졌을 때 그 숫자의 다양성을 구하는 프로그램을 작성하라.

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T(1 ≤ T ≤ 100)가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 다양성을 체크하고 싶은 숫자 X(1 ≤ X ≤ 109) 가 주어진다.

# [출력]

# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 주어진 숫자의 다양성을 출력하라.

for t in range(int(input())):      # T입력받기
    a = {}                         # n : 개수
    for n in input():              # input으로 받은 문자 1글자씩 돌리기
        if n not in a.keys():      # n이 key에 없으면
            a[n] = 1               # n : 1로 저장
        else:                      # n이 key에 있으면
            a[n] += 1              # n : a[n]+1로 저장
    print(f"#{t+1}", len(a.keys()))# a의 key 개수를 출력


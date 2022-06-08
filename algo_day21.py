#!/usr/bin/env python
# coding: utf-8

# In[18]:


# 문제 출처 : SW Expert Academy

# 현주는 1번부터 N번까지 N개의 상자를 가지고 있다.
# 각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0으로 적혀있다.

# 숫자가 너무 단조로웠던 현주는 
# 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 한다. 
# 변경하는 방법은 다음과 같다.

# i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경

# 현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 정수 N, Q (1 ≤ N, Q ≤ 103)가 공백으로 구분되어 주어진다.
# 다음 Q개의 줄의 i번째 줄에는 Li, Ri (1 ≤ Li ≤ Ri ≤ N)이 주어진다.


# [출력]

# 각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 각 테스트 케이스마다 Q개의 작업을 수행한 다음 1번부터 N번까지의 상자에 적혀있는 값들을 순서대로 출력한다.

# [input 예시]
# 1 // Test Case 개수
# 5 2 // 첫 번째 Test Case, N=5, Q=2
# 1 3 // i = 1일 때, L=1, R=3
# 2 4	// i = 2일 때, L=2, R=4

# [output 예시]
# #1 1 2 2 2 0	//첫 번째 테스트케이스 결과

for t in range(int(input())):            # T값 입력 받기
    N, Q = map(int, input().split())     # N, Q 값 입력 받기
    N = [0 for n in range(1, N+1)]       # N개의 0이 요소로 있는 리스트 만들기
    for i in range(1, Q+1):              # Q개의 작업 요소 돌리기
        L, R = map(int, input().split()) # L, R 값 입력 받기
        for index in range(L-1, R):      # list에 인덱스 L-1:R 범위의 값을 i로 변경
            N[index] = i
    print(f"#{t+1}",end=' ');print(*N)   # test case와 변경된 list 값 출력

